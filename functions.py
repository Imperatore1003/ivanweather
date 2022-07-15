import urllib.parse
import json
import http
import requests

def recentCities(cities):
    """Returns a list of recent cities"""

    cities = json.loads(cities)

    history = []

    if cities != []:
        for city in cities:
            history.append({"name": city, "url": urllib.parse.quote(city)})

        return history
    
    return [{"name": "No recent cities", "url": "noRecentCities"}]

def api():
    conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "39a36a1af4msh4c0c2be2d82278cp10e88cjsn79a0c89c3bb9",
        'X-RapidAPI-Host': "community-open-weather-map.p.rapidapi.com"
        }

    conn.request("GET", "/weather?q=Alghero%2Cit&callback=test&lang=en&units=metric&mode=xml", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))