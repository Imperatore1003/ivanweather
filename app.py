from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

import json
from datetime import datetime

from functions import recentCities, api

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# @app.before_request
# def before_request():
#     if not request.is_secure:
#         url = request.url.replace('http://', 'https://', 1)
#         code = 301
#         return redirect(url, code=code)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    """Show the homepage of IvanWeather"""

    # init()

    # cities = recentCities(session["history"])

    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    """Show results of search"""

    # init()
    
    # cities = recentCities(session["history"])
    cityName = request.args.get("city")

    result = api(cityName)
    city = json.loads(result)
    city["main"]["pressure"] = round(city["main"]["pressure"] / 33.864 , 2)
    city["sys"]["sunrise"] = datetime.fromtimestamp(int(city["sys"]["sunrise"])).strftime('%H:%M:%S')
    city["sys"]["sunset"] = datetime.fromtimestamp(int(city["sys"]["sunset"])).strftime('%H:%M:%S')

    # if city == "noRecentCities":
    #     return redirect("/")

    # session["history"] = str(json.loads(session["history"]).append(city))

    return render_template("search.html", city=city)

@app.route("/google08e23da205bdc745.html")
def verification():
    """Verify Google Search Console"""
    return render_template("google08e23da205bdc745.html")
@app.route("/robots.txt")
def robots():
    """robots.txt"""
    return render_template("robots.txt")
@app.route("/sitemap.xml")
def sitemap():
    """Sitemap"""
    return render_template("sitemap.xml")
@app.route("/manifest.json")
def manifest():
    """Manifest"""
    return render_template("manifest.json")
@app.route("/browserconfig.xml")
def browserconfig():
    """Browserconfig"""
    return render_template("browserconfig.xml")

# def init():
#     if session.get("history") == None:
#         session["history"] = "[]"

if __name__ == "__main__":
    app.run()

# @app.route("/.well-known/acme-challenge/OKitNQ-pFR_TSZw-sNbfUIDH6cPWggl_UFt3tMIV8Jw")
# def acme_challenge():
#     return render_template("ssl.html")