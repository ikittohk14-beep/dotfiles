import json
import os
import sys
import time
import urllib.request

CACHE_FILE = os.path.expanduser("~/.cache/waybar-weather.json")
CACHE_MAX_AGE = 900

WEATHER_ICONS = {
    "113": ("󰖙", "Ясно"),
    "116": ("󰖕", "Переменная облачность"),
    "119": ("󰖐", "Облачно"),
    "122": ("󰖐", "Пасмурно"),
    "143": ("󰖑", "Дымка"),
    "248": ("󰖑", "Туман"),
    "260": ("󰖑", "Ледяной туман"),
    "176": ("󰖖", "Небольшой дождь"),
    "263": ("󰖖", "Мелкая морось"),
    "266": ("󰖖", "Морось"),
    "293": ("󰖖", "Небольшой дождь"),
    "296": ("󰖖", "Умеренный дождь"),
    "299": ("󰖖", "Ливневый дождь"),
    "302": ("󰖖", "Сильный дождь"),
    "305": ("󰖖", "Ливень"),
    "308": ("󰖖", "Сильный ливень"),
    "353": ("󰖖", "Небольшой ливень"),
    "356": ("󰖖", "Ливень"),
    "359": ("󰖖", "Проливной дождь"),
    "200": ("󰖓", "Гроза"),
    "386": ("󰖓", "Гроза с дождем"),
    "389": ("󰖓", "Сильная гроза"),
    "179": ("󰖘", "Снег"),
    "227": ("󰖘", "Метель"),
    "230": ("󰖘", "Снегопад"),
    "323": ("󰖘", "Небольшой снег"),
    "326": ("󰖘", "Умеренный снег"),
    "329": ("󰖘", "Снегопад"),
    "332": ("󰖘", "Сильный снегопад"),
}

def get_cached_data():
    if os.path.exists(CACHE_FILE):
        try:
            mtime = os.path.getmtime(CACHE_FILE)
            if time.time() - mtime < CACHE_MAX_AGE:
                with open(CACHE_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
    return None

def fetch_weather():
    try:
        req = urllib.request.Request(
            "https://wttr.in/?format=j1",
            headers={"User-Agent": "curl/8.0.0"}
        )
        with urllib.request.urlopen(req, timeout=3.5) as res:
            data = json.loads(res.read().decode("utf-8"))
            os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f)
            return data
    except Exception:

        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
    return None

def main():
    data = get_cached_data()
    if not data:
        data = fetch_weather()

    if not data or "current_condition" not in data or not data["current_condition"]:
        print(json.dumps({"text": "☁ --°C", "tooltip": "Погода недоступна"}))
        return

    curr = data["current_condition"][0]
    temp = curr.get("temp_C", "--")
    feels = curr.get("FeelsLikeC", temp)
    humidity = curr.get("humidity", "--")
    wind_kmph = curr.get("windspeedKmph", "--")
    code = curr.get("weatherCode", "119")

    icon, desc = WEATHER_ICONS.get(code, ("☁", curr.get("weatherDesc", [{}])[0].get("value", "Облачно")))

    temp_str = f"+{temp}°C" if int(temp) > 0 else f"{temp}°C" if temp != "--" else "--°C"
    feels_str = f"+{feels}°C" if int(feels) > 0 else f"{feels}°C" if feels != "--" else "--°C"

    area = ""
    try:
        nearest = data.get("nearest_area", [{}])[0]
        area = nearest.get("areaName", [{}])[0].get("value", "")
    except Exception:
        pass

    location_header = f" {area} • " if area else ""
    tooltip = (
        f"{location_header}{desc}\n"
        f"Температура: {temp_str} (ощущается как {feels_str})\n"
        f"Влажность: {humidity}%\n"
        f"Ветер: {wind_kmph} км/ч"
    )

    out = {
        "text": f"{icon} {temp_str}",
        "tooltip": tooltip,
        "class": "weather"
    }
    print(json.dumps(out, ensure_ascii=False))

if __name__ == "__main__":
    main()
