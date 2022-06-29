import urllib.parse

def recentCities(cities):
    """Returns a list of recent cities"""

    history = []

    if cities != []:
        for city in cities:
            history.append({"name": city, "url": urllib.parse.quote(city)})

        return history
    
    return [{"name": "No recent cities", "url": "noRecentCities"}]