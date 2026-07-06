# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "prettytable>=3.17.0",
#     "requests>=2.33.1",
#     "rich>=15.0.0",
# ]
# ///

import requests
import json
from datetime import datetime

from rich.table import Table
from rich.console import Console

icons = {
    2: "",
    3: "󰖗",
    4: "",
    5: "󰖗",
    6: "󰼶",
    7: "󰖑",
    8: "",
}


def space(a, b=10):
    return " " * (b - a)


def main() -> None:
    table = Table(show_header=True, header_style="bold")

    city_json = open("/home/msjtw/.config/waybar/city.json", "r")
    city_data = json.load(city_json)
    city_json.close()
    lat = city_data[0]["lat"]
    lon = city_data[0]["lon"]
    city_name = city_data[0]["name"]
    city_name += space(len(city_name), 15)

    key_file = open("/home/msjtw/Documents/DOTFILES/key", "r")
    api_key = key_file.read().strip()
    r = requests.get(
        f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={
            lon
        }&exclude=minutely&appid={api_key}&units=metric"
    )
    data = json.loads(r.text)

    time_offset = data["timezone_offset"]

    current = data["current"]
    now = f" {current['feels_like']}°C /  {current['wind_speed']}m/s / {
        icons[current['weather'][0]['id'] // 100]
    }{current['weather'][0]['main']}"

    current_time = datetime.fromtimestamp(current["dt"]).strftime("%H:%M")
    sunrise = datetime.fromtimestamp(current["sunrise"]).strftime("%H:%M")
    sunset = datetime.fromtimestamp(current["sunset"]).strftime("%H:%M")

    hourly = []
    hourly_json = data["hourly"]

    for i in range(13):
        time = datetime.fromtimestamp(hourly_json[i]["dt"]).strftime("%H:%M")
        time += space(len(time))
        group = hourly_json[i]["weather"][0]["id"] // 100
        main = f"{icons[group]} " + str(hourly_json[i]["weather"][0]["main"])
        main += space(len(main))
        temp = " " + str(hourly_json[i]["temp"]) + " °C"
        temp += space(len(temp))
        feel = " " + str(hourly_json[i]["feels_like"]) + " °C"
        feel += space(len(feel))
        wind = str(hourly_json[i]["wind_speed"]) + " m/s"
        wind += space(len(wind))
        prec = str(int(hourly_json[i]["pop"] * 100)) + "%"
        prec += space(len(prec), 6)
        if group == 5 or group == 6:
            vol = str(hourly_json[i][main[1:].lower().strip()]["1h"]) + "mm"
            prec += vol
        table.add_row(time, main, temp, feel, wind, prec)

    # table.add_row(divider=True)
    table.add_section()
    daily = []
    daily_json = data["daily"]

    for i in range(5):
        time = datetime.fromtimestamp(daily_json[i]["dt"]).strftime("%A")
        time += space(len(time))
        group = daily_json[i]["weather"][0]["id"] // 100
        main = f"{icons[group]} " + str(daily_json[i]["weather"][0]["main"])
        main += space(len(main))
        temp = "" + str(daily_json[i]["temp"]["day"]) + "°C"
        temp += space(len(temp))
        feel = "" + str(daily_json[i]["feels_like"]["day"]) + "°C"
        feel += space(len(feel))
        wind = str(daily_json[i]["wind_speed"]) + "m/s"
        wind += space(len(wind))
        prec = str(int(daily_json[i]["pop"] * 100)) + "%"
        prec += space(len(prec), 6)
        if group == 5 or group == 6:
            vol = str(daily_json[i][main[1:].lower().strip()]) + "mm"
            prec += vol
        summ = str(daily_json[i]["summary"])
        table.add_row(time, main, temp, feel, wind, prec)
        table.add_row(sum, colspan=len(table.columns))

    print(table)

    ret = {}
    ret["text"] = now
    ret["tooltip"] = (
        city_name
        + "   "
        + sunrise
        + "\t   "
        + sunset
        + "\n---\n"
        + hourly[1]
        + hourly[2]
        + hourly[3]
        + hourly[4]
        + hourly[6]
        + hourly[8]
        + hourly[10]
        + hourly[12]
        + "---\n"
        + daily[1]
        + daily[2]
        + daily[3]
        + daily[4]
    )
    ret["class"] = ("weather",)
    ret["percentage"] = "0"

    print(json.dumps(ret))


if __name__ == "__main__":
    main()
