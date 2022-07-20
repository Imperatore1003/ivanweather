import re
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from flask_compress import Compress
from tempfile import mkdtemp

import json

from functions import recentCities, api

app = Flask(__name__)
Compress(app)
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

@app.route("/", methods=['GET', 'POST'])
def index():
    """Show the homepage of IvanWeather"""
    if request.method == "POST":
        output = request.get_json()
        result = str(json.loads(output))

        session["cords"] = result

        return redirect("/")
    
    elif request.method == "GET":

        if session.get("cords") is None:
            return render_template("index.html", getCords=1)
        else:
            cords = json.loads(session["cords"].replace("'", '"'))
            latitude = cords["latitude"]
            longitude = cords["longitude"]

            city = api(0, latitude, longitude, 1)

            return render_template("index.html", getCords=0, city=city)

@app.route("/search", methods=["GET", "POST"])
def search():
    """Show results of search"""

    cityName = request.args.get("city")

    city = api(cityName)

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
@app.route("/sw.js")
def serviceWorker():
    """Browserconfig"""
    return render_template("sw.js")
# @app.route("/.well-known/acme-challenge/OKitNQ-pFR_TSZw-sNbfUIDH6cPWggl_UFt3tMIV8Jw")
# def acme_challenge():
#     return render_template("ssl.html")

if __name__ == "__main__":
    app.run()