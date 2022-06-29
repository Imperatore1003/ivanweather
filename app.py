from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

import json

from functions import recentCities

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

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

    init()

    cities = recentCities(session["history"])

    return render_template("index.html", cities=cities)

@app.route("/search", methods=["GET", "POST"])
def search():
    """Show results of search"""

    init()
    
    cities = recentCities(session["history"])
    city = request.args.get("city")

    if city == "noRecentCities":
        return redirect("/")

    session["history"] = str(json.loads(session["history"]).append(city))

    return render_template("search.html", city=city, cities=cities)

def init():
    if session.get("history") == None:
        session["history"] = "[]"

if __name__ == "__main__":
    app.run()
