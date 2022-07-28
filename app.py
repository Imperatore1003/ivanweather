from random import random
from flask import Flask, flash, redirect, render_template, request, session, Response, send_from_directory
from flask_session import Session
from flask_compress import Compress
from tempfile import mkdtemp

import json
from random import random

from functions import api

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

        ranNum = int(random() * 10000)

        if session.get("cords") is None:
            return render_template("index.html", getCords=1, ranNum=ranNum)
        else:
            cords = json.loads(session["cords"].replace("'", '"'))
            latitude = cords["latitude"]
            longitude = cords["longitude"]

            if session.get("units") is None:
                session["units"] = 0
            check = 0 if int(session["units"]) == 0 else 1

            city = api(0, latitude, longitude, 1, session["units"])


            return render_template("index.html", getCords=0, city=city, check=check, ranNum=ranNum)

@app.route("/search", methods=["GET", "POST"])
def search():
    """Show results of search"""

    cityName = request.args.get("city")

    if session.get("units") is None:
        session["units"] = 0
    check = 0 if int(session["units"]) == 0 else 1

    city = api(cityName, 0, 0, 0, session["units"])

    return render_template("search.html", city=city, check=check)

@app.route("/setUnits", methods=['POST'])
def units():
    """Set units"""
    if request.method == "POST":
        output = request.get_json()
        result = json.loads(output)

        # session["units"] = "imperial" if result["units"] == 0 else "metric"
        session["units"] = int(result["units"])

        return redirect(result["url"])

@app.route('/<path:filename>')
def download_file(filename):
    MEDIA_FOLDER = "media"
    return send_from_directory(MEDIA_FOLDER, filename, as_attachment=False)

@app.route("/fallback")
def fallback():
    """Fallback page"""
    return render_template("fallback.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden_page(e):
    return render_template('403.html'), 403

@app.errorhandler(410)
def gone_page(e):
    return render_template('410.html'), 410

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route("/google08e23da205bdc745.html")
def verification():
    """Verify Google Search Console"""
    return render_template("google08e23da205bdc745.html")

@app.route("/.well-known/acme-challenge/DXBAoCp54ZmucFSSbB3YknNsgMhKxRIjUEyqWQmxjjU")
def ssl():
    """Let's Encrypt"""
    return render_template("ssl.html")

@app.route("/robots.txt")
def robots():
    """robots.txt"""
    file = ""
    with open('robots.txt') as f:
        file = f.readlines()
    return Response(file, mimetype='text/plain')

@app.route("/sitemap.xml")
def sitemap():
    """Sitemap"""
    return render_template("sitemap.xml")

@app.route("/manifest.json")
def manifest():
    """Manifest"""
    file = ""
    with open('manifest.json') as f:
        file = f.readlines()
    return Response(file, mimetype='application/json')

@app.route("/browserconfig.xml")
def browserconfig():
    """Browserconfig"""
    return render_template("browserconfig.xml")

@app.route("/sw.js")
def serviceWorker():
    """Service Worker"""
    file = ""
    with open('sw.js') as f:
        file = f.readlines()
    return Response(file, mimetype='application/javascript')

if __name__ == "__main__":
    app.run()