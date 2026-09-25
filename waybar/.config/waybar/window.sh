#!/usr/bin/env bash

MAX_TITLE_LEN=20

get_window() {

    if command -v wlrctl >/dev/null 2>&1; then
        active=$(wlrctl toplevel list state:active 2>/dev/null | head -n 1)
        if [[ -n "$active" && "$active" == *:* ]]; then
            app="${active%%:*}"
            title="${active#*: }"
            echo "$app::$title"
            return
        fi
        last=$(wlrctl toplevel list 2>/dev/null | tail -n 1)
        if [[ -n "$last" && "$last" == *:* ]]; then
            app="${last%%:*}"
            title="${last#*: }"
            echo "$app::$title"
            return
        fi
    fi

    if command -v hyprctl >/dev/null 2>&1; then
        w=$(hyprctl activewindow -j 2>/dev/null)
        cls=$(jq -r '.class // empty' <<< "$w" 2>/dev/null)
        tit=$(jq -r '.title // empty' <<< "$w" 2>/dev/null)
        if [[ -n "$cls" && "$cls" != "null" ]]; then
            echo "$cls::$tit"
            return
        fi
    fi

    echo "Desktop::Workspace"
}

print_status() {
    res=$(get_window)
    app="${res%%::*}"
    title="${res#*::}"

    case "$app" in
        "zen"|"zen-bin") app="Zen Browser" ;;
        "kitty") app="Kitty" ;;
        "org.telegram.desktop") app="Telegram" ;;
        "org.gnome.Nautilus") app="Files" ;;
        "Spotify") app="Spotify" ;;
        "com.follow.clashx") app="Clash" ;;
        "org.gnome.TextEditor") app="Editor" ;;
        "drift-shell-settings") app="Settings" ;;
    esac

    if (( ${
        title="${title:0:$((MAX_TITLE_LEN-3))}..."
    fi

    esc_top=$(sed 's/&/&amp;/g; s/</&lt;/g; s/>/&gt;/g' <<< "$app")
    esc_bottom=$(sed 's/&/&amp;/g; s/</&lt;/g; s/>/&gt;/g' <<< "$title")

    text="<span size='7500' foreground='#a6adc8' rise='-2000'>$esc_top</span>
<span size='9000' weight='bold' foreground='#ffffff'>$esc_bottom</span>"

    tooltip="$app: $title"

    jq -nc \
        --arg text "$text" \
        --arg tooltip "$tooltip" \
        '{ text: $text, class: "custom-window", tooltip: $tooltip }'
}

print_status

last=""
while true; do
    current=$(get_window)
    if [[ "$current" != "$last" ]]; then
        print_status
        last="$current"
    fi
    sleep 0.8
done
