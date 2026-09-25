import sys
import json
import subprocess

MAX_LEN = 22

def get_players():
    try:
        out = subprocess.check_output(
            ['playerctl', '-a', 'metadata', '--format', '{{playerName}}|{{status}}|{{artist}}|{{title}}|{{album}}'],
            text=True, stderr=subprocess.DEVNULL
        ).strip()
        if not out:
            return []
        players = []
        for line in out.split('\n'):
            line = line.strip()
            if not line:
                continue
            parts = line.split('|')
            if len(parts) >= 5:
                players.append({
                    'name': parts[0].strip(),
                    'status': parts[1].strip(),
                    'artist': parts[2].strip(),
                    'title': parts[3].strip(),
                    'album': parts[4].strip()
                })
        return players
    except Exception:
        return []

def choose_player(players):
    if not players:
        return None
    def score(p):
        is_spotify = 'spotify' in p['name'].lower()
        status = p['status'].lower()

        if is_spotify and status == 'playing':
            return 1000

        elif not is_spotify and status == 'playing':
            return 800

        elif is_spotify and status == 'paused' and p['title']:
            return 600

        elif not is_spotify and status == 'paused' and p['title']:
            return 200
        elif is_spotify:
            return 50
        else:
            return 10
    players.sort(key=score, reverse=True)
    return players[0]

def handle_action(action):
    players = get_players()
    chosen = choose_player(players)
    if chosen:
        subprocess.run(['playerctl', '-p', chosen['name'], action], stderr=subprocess.DEVNULL)
    else:
        subprocess.run(['playerctl', '--player=spotify,%any', action], stderr=subprocess.DEVNULL)

def main():
    if len(sys.argv) > 2 and sys.argv[1] == '--action':
        handle_action(sys.argv[2])
        return

    players = get_players()
    chosen = choose_player(players)

    if not chosen or not chosen.get('title'):
        print(json.dumps({
            "text": "󰎆  No media ",
            "tooltip": "Нет активного медиа",
            "class": "none"
        }, ensure_ascii=False))
        return

    title = chosen['title']
    artist = chosen['artist']
    album = chosen['album']
    status = chosen['status']
    name = "Spotify" if "spotify" in chosen['name'].lower() else chosen['name'].capitalize()

    if len(title) > MAX_LEN:
        display_title = title[:MAX_LEN - 1].rstrip() + "…"
    else:
        display_title = title

    icon = "󰎆"
    text = f"{icon}  {display_title} "

    status_ru = "Воспроизведение" if status.lower() == "playing" else "Пауза"
    tooltip_lines = [
        f"{name} • {status_ru}",
        f"Трек: {title}"
    ]
    if artist:
        tooltip_lines.append(f"Исполнитель: {artist}")
    if album:
        tooltip_lines.append(f"Альбом: {album}")
    tooltip_lines.append("\n(ЛКМ: Пауза/Плей • ПКМ: След. • СКМ: Пред.)")

    cls = [status.lower()]
    if 'spotify' in chosen['name'].lower():
        cls.append('spotify')
    else:
        cls.append('other')

    out = {
        "text": text,
        "tooltip": "\n".join(tooltip_lines),
        "class": " ".join(cls)
    }
    print(json.dumps(out, ensure_ascii=False))

if __name__ == '__main__':
    main()
