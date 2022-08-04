# IvanWeather
## Video Demo: https://youtu.be/FTDHOeG9krM
## Site: [ivanweather.com](https://ivanweather.com)
## Description:
IvanWeather is a weather service that returns the local weather of a given city.

Weather services are commonly used every day by everyone to check the weather in their city.

The site will prompt you to access your location on the homepage and it will display your weather in a nice card created with bootstrap or you can search for a city in the search bar at the top right of the screen. If you are using a mobile you have to open the hamburger menu in order to access the search bar.

This project uses an API offered by [OpenWeather](https://openweathermap.org/)

## Implementation
The main files of the project are [`app.py`](/app.py) and [`functions.py`](/functions.py).

#### [`app.py`](/app.py)
This is the application's core where the web server is being executed.

#### [`functions.py`](/functions.py)
In this file are included the functions required to run [`app.py`](/app.py)

### Additional files
There are other files that are needed to run the site:

#### [`templates folder`](/templates/)
The template folders contain all the HTML files of the site:
- [`index.html`](/templates/index.html)
    - This file contains the javascript code for getting the coordinates of the client from the browser.
- [`search.html`](/templates/search.html);
- [`layout.html`](/templates/layout.html)
    - This file contains the head tag and the top bar HTML code and includes two javascript files.
- [`fallback.html`](/templates/fallback.html)
    - This file is loaded by the service worker when there is no connection.
- [`404 error code`](/templates/404.html)
    - This is the file that is shown when there is a 404 error in the server. Are available:
        - [`404`](/templates/404.html)
        - [`403`](/templates/403.html)
        - [`410`](/templates/410.html)
        - [`500`](/templates/500.html)
- [`weatherCard.html`](/templates/weatherCard.html)
    - This file is only a layout page that can be included for displaying nicely the weather information of a city.

#### [`static folder`](/static/)
The static folder contains nondynamic files such as images and more:
- [`main.js`](/static/main.js)
    - This is the main javascript file of the site and it registers the service worker.
- [`style.css`](/static/style.css)
    - This file contains the CSS rules that it cannot use with bootstrap.
- [`img folder`](/static/img/)
    - This folder contains all the images of the site.
        - Apple icons
        - Android icons
        - Favicons
        - Ms icons

- [`media folder`](/media/)
    - It contains the files that are needed to be in the root directory.

#### [`manifest.json`](/manifest.json)
- It is a file required to create a [PWA](https://it.wikipedia.org/wiki/Progressive_Web_App) (Progressive Web App) and declares some site's settings.

#### [`Procfile`](/Procfile)
- Is a file used by [Heroku](https://heroku.com) (the hosting service I decided to use for this app).

#### [`requirements.txt`](/requirements.txt)
- This is another file used by [Heroku](https://heroku.com), where are declared the python libraries used for this project.

#### [`robots.txt`](/robots.txt)
- This file is used by the web crawlers in which are declared the folders that cannot be accessed.

#### [`sw.js`](/sw.js)
- This file is the service worker used to cache files so they can be accessed offline.

#### [`TODO`](/TODO)
- In this file I wrote all the ideas to develop for this project.

### ALL THE API KEYS STORED IN THIS REPOSITORY ARE DEACTIVATED AND USELESS. THIS PROJECT USES SYSTEM VARIABLES TO STORE THE API KEY.
