import urllib.parse
import json
from datetime import datetime
import urllib.request
import urllib.parse

def recentCities(cities):
    """Returns a list of recent cities"""

    cities = json.loads(cities)

    history = []

    if cities != []:
        for city in cities:
            history.append({"name": city, "url": urllib.parse.quote(city)})

        return history
    
    return [{"name": "No recent cities", "url": "noRecentCities"}]

def api(city, cord1 = 0, cord2 = 0, mode = 0, unit = 0):

    # city = json.loads("{'coord': {'lon': 8.3213, 'lat': 40.5587}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': 28.01, 'feels_like': 28.55, 'temp_min': 28.01, 'temp_max': 28.01, 'pressure': 1016, 'humidity': 51}, 'visibility': 10000, 'wind': {'speed': 1.54, 'deg': 80}, 'clouds': {'all': 0}, 'dt': 1658263786, 'sys': {'type': 1, 'id': 6717, 'country': 'IT', 'sunrise': 1658203902, 'sunset': 1658256834}, 'timezone': 7200, 'id': 3183284, 'name': 'Alghero', 'cod': 200}".replace("'", '"'))

    units = "imperial" if unit == 0 else "metric"

    prefix = ""
    preprefix = "https://api.openweathermap.org/data/2.5/weather?"
    suffix = "&appid=cfdec8014b5fefbdaeb3c9793299b335"

    if mode == 0:
        city = urllib.parse.quote(city)

        prefix = f"q={city}"
    elif mode == 1:
        prefix = f"lat={cord1}&lon={cord2}"

    myAPI = preprefix + prefix + f"&lang=en&units={units}" + suffix
    myAPI = preprefix + prefix + f"&lang=en&units=metric" + suffix

    city = {}
    with urllib.request.urlopen(myAPI) as url:
        city = json.loads(url.read().decode())

    # print(str(city))

    if unit == 1:
        city["wind"]["speed"] = round(city["wind"]["speed"] * 3.6, 2) # from m/s to km/h
        city["dewPoint"] = round(city["main"]["temp"] - ((100 - city["main"]["humidity"]) / 5), 2)
        city["sys"]["sunrise"] = datetime.fromtimestamp(int(city["sys"]["sunrise"])).strftime('%H:%M:%S')
        city["sys"]["sunset"] = datetime.fromtimestamp(int(city["sys"]["sunset"])).strftime('%H:%M:%S')

        city["units"] = {"wind": "km/h", "pressure": "hPa"}

    else:
        temp = city["main"]["temp"]
        city["dewPoint"] = toFahrenheit(round(temp - ((100 - city["main"]["humidity"]) / 5), 2))
        city["main"]["temp_max"] = toFahrenheit(city["main"]["temp_max"])
        city["main"]["temp_min"] = toFahrenheit(city["main"]["temp_min"])
        city["main"]["feels_like"] = toFahrenheit(city["main"]["feels_like"])
        city["main"]["temp"] = toFahrenheit(city["main"]["temp"])
        city["wind"]["speed"] = round(city["wind"]["speed"] * 2.237, 2) # from m/s to mph
        city["main"]["pressure"] = round(city["main"]["pressure"] / 33.864 , 2) # from hPa to inches of mercury
        city["sys"]["sunrise"] = datetime.fromtimestamp(int(city["sys"]["sunrise"])).strftime('%I:%M:%S %p')
        city["sys"]["sunset"] = datetime.fromtimestamp(int(city["sys"]["sunset"])).strftime('%I:%M:%S %p')

        city["units"] = {"wind": "mph", "pressure": "in"}

    # print(str(city))

    return city

def toFahrenheit(temp):
    return round((temp * 9/5) + 32, 2)