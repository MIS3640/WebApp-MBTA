"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near, distancetostation


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        location = request.form["location"]
        mbta, wheelchair = find_stop_near(location)
        if mbta != "No location found": 
            return render_template("mbta_station.html", mbta=mbta, wheelchair=wheelchair, distance=distance)
        else:
            return render_template('error_page.html')
    return render_template("index.html")

