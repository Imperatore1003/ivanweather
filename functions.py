import urllib.parse
import json
import http
from datetime import datetime
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

def api(city, cord1 = 0, cord2 = 0, mode = 0):

    data = '{"coord":{"lon":8.3181,"lat":40.5589},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":78.89,"feels_like":78.89,"temp_min":78.89,"temp_max":78.89,"pressure":1016,"humidity":89},"visibility":10000,"wind":{"speed":1.14,"deg":0},"clouds":{"all":0},"dt":1658002619,"sys":{"type":1,"id":6717,"country":"IT","sunrise":1657944556,"sunset":1657997751},"timezone":7200,"id":3183284,"name":"Alghero","cod":200}'

    # conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

    # headers = {
    #     'X-RapidAPI-Key': "39a36a1af4msh4c0c2be2d82278cp10e88cjsn79a0c89c3bb9",
    #     'X-RapidAPI-Host': "community-open-weather-map.p.rapidapi.com"
    #     }

    # if mode == 0:
    #     city = urllib.parse.quote(city)

    #     conn.request("GET", f"/weather?q={city}&lang=en&units=metric", headers=headers)
    # elif mode == 1:
    #     conn.request("GET", f"/weather?lat={cord1}&lon={cord2}&lang=en&units=metric", headers=headers)

    # res = conn.getresponse()
    # data = res.read()

    # data = str(data.decode("utf-8"))

    city = json.loads(data)
    city["main"]["pressure"] = round(city["main"]["pressure"] / 33.864 , 2)
    city["sys"]["sunrise"] = datetime.fromtimestamp(int(city["sys"]["sunrise"])).strftime('%H:%M:%S')
    city["sys"]["sunset"] = datetime.fromtimestamp(int(city["sys"]["sunset"])).strftime('%H:%M:%S')

    return city