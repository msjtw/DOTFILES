import requests
import json
from datetime import datetime

def space(a, b=10):
    return ' '*(b-a)

icons = {
    2: "",
    3: "󰖗",
    4: "",
    5: "󰖗",
    6: "󰼶",
    7: "󰖑",
    8: "",
}

clouds = {

}


city_json = open('/home/msjtw/.config/waybar/city.json', "r")
city_data = json.load(city_json) 
city_json.close()
lat = city_data[0]["lat"]
lon = city_data[0]["lon"]
city_name = city_data[0]["name"]
city_name += space(len(city_name), 15)

api_key = "7acaae7aee25aa7e5a5cabd98eb57132"
r = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely&appid={api_key}&units=metric')
data = json.loads(r.text)

time_offset = data['timezone_offset']

current = data["current"]
now = f' {current['feels_like']}°C /  {current['wind_speed']}m/s / {icons[current['weather'][0]['id']//100]}{current['weather'][0]['main']}'

current_time = datetime.fromtimestamp(current['dt']).strftime('%H:%M')

hourly = []
hourly_json = data["hourly"]

for i in range(13):
    time = datetime.fromtimestamp(hourly_json[i]['dt']).strftime('%H:%M')
    time += space(len(time))
    group = hourly_json[i]['weather'][0]['id']//100
    main = f'{icons[group]} ' + str(hourly_json[i]['weather'][0]['main'])
    main += space(len(main))
    temp = '' + str(hourly_json[i]['temp']) + '°C'
    temp += space(len(temp)) 
    feel = '' + str(hourly_json[i]['feels_like']) + '°C'
    feel += space(len(feel))
    wind = str(hourly_json[i]['wind_speed']) + 'm/s'
    wind += space(len(wind))
    prec = str(int(hourly_json[i]['pop']*100)) + '%'
    prec += space(len(prec), 6)
    if (group == 5 or group == 6):
        vol = str(hourly_json[i][main[1:].lower().strip()]['1h']) + 'mm'
        prec += vol
    hourly.append(time+main+temp+feel+wind+prec+'\n')

daily = []
daily_json = data["daily"]

for i in range(5):
    time = datetime.fromtimestamp(daily_json[i]['dt']).strftime('%A')
    time += space(len(time))
    group = daily_json[i]['weather'][0]['id']//100
    main = f'{icons[group]} ' + str(daily_json[i]['weather'][0]['main'])
    main += space(len(main))
    temp = '' + str(daily_json[i]['temp']['day']) + '°C'
    temp += space(len(temp)) 
    feel = '' + str(daily_json[i]['feels_like']['day']) + '°C'
    feel += space(len(feel))
    wind = str(daily_json[i]['wind_speed']) + 'm/s'
    wind += space(len(wind))
    prec = str(int(daily_json[i]['pop']*100)) + '%'
    prec += space(len(prec), 6)
    if (group == 5 or group == 6):
        vol = str(daily_json[i][main[1:].lower().strip()]) + 'mm'
        prec += vol
    summ = str(daily_json[i]['summary'])
    daily.append(time+main+temp+feel+wind+prec+'\n'+summ+'\n')

ret = {}
ret['text'] = now
ret['tooltip'] = city_name + current_time + "\n---\n" + hourly[1] + hourly[2] + hourly[3] + hourly[4] + hourly[6] + hourly[8] + hourly[10] + hourly[12] + '---\n' + daily[1] + daily[2] + daily[3] + daily[4]
ret['class'] = "weather",
ret['percentage'] = "0"

print(json.dumps(ret))