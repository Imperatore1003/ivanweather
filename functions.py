import urllib.parse
import json

def recentCities(cities):
    """Returns a list of recent cities"""

    cities = json.loads(cities)

    history = []

    if cities != []:
        for city in cities:
            history.append({"name": city, "url": urllib.parse.quote(city)})

        return history
    
    return [{"name": "No recent cities", "url": "noRecentCities"}]