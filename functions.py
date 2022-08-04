import urllib.parse
import urllib.request
import urllib.parse

import os
import json
from datetime import datetime

def api(cityName, cord1 = 0, cord2 = 0, mode = 0, unit = 0):

    api = os.environ.get("WEATHER_API")
    
    units = "imperial" if unit == 0 else "metric"

    prefix = ""
    preprefix = "https://api.openweathermap.org/data/2.5/weather?"
    suffix = "&appid=" + api

    if mode == 0:
        cityName = urllib.parse.quote(cityName)

        prefix = f"q={cityName}"
    elif mode == 1:
        prefix = f"lat={cord1}&lon={cord2}"

    myAPI = preprefix + prefix + f"&lang=en&units={units}" + suffix
    myAPI = preprefix + prefix + f"&lang=en&units=metric" + suffix

    city = {}
    with urllib.request.urlopen(myAPI) as url:
        city = json.loads(url.read().decode())

    city["sys"]["sunrise"] = city["sys"]["sunrise"] + city["timezone"]
    city["sys"]["sunset"] = city["sys"]["sunset"] + city["timezone"]

    if unit == 1:
        city["wind"]["speed"] = round(city["wind"]["speed"] * 3.6, 2) # from m/s to km/h
        city["dewPoint"] = round(city["main"]["temp"] - ((100 - city["main"]["humidity"]) / 5), 2)
        city["sys"]["sunrise"] = datetime.fromtimestamp(city["sys"]["sunrise"]).strftime('%H:%M:%S')
        city["sys"]["sunset"] = datetime.fromtimestamp(city["sys"]["sunset"]).strftime('%H:%M:%S')

        city["units"] = {"wind": "km/h", "pressure": "hPa", "visibility": "km"}

    else:
        temp = city["main"]["temp"]
        city["dewPoint"] = toFahrenheit(round(temp - ((100 - city["main"]["humidity"]) / 5), 2))
        city["main"]["temp_max"] = toFahrenheit(city["main"]["temp_max"])
        city["main"]["temp_min"] = toFahrenheit(city["main"]["temp_min"])
        city["main"]["feels_like"] = toFahrenheit(city["main"]["feels_like"])
        city["main"]["temp"] = toFahrenheit(city["main"]["temp"])
        city["wind"]["speed"] = round(city["wind"]["speed"] * 2.237, 2) # from m/s to mph
        city["main"]["pressure"] = round(city["main"]["pressure"] / 33.864 , 2) # from hPa to inches of mercury
        city["sys"]["sunrise"] = datetime.fromtimestamp(city["sys"]["sunrise"]).strftime('%I:%M:%S %p %z')
        city["sys"]["sunset"] = datetime.fromtimestamp(city["sys"]["sunset"]).strftime('%I:%M:%S %p %z')
        city["visibility"] = round(city["visibility"] / 1.609, 2)

        city["units"] = {"wind": "mph", "pressure": "in", "visibility": "mi"}

    return city

def toFahrenheit(temp):
    return round((temp * 9/5) + 32, 2)