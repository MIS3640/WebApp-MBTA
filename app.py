"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        location = request.form["location"]
        mbta, wheelchair = find_stop_near(location)
        return render_template("mbta_station.html", mbta=mbta, wheelchair=wheelchair)
    return render_template("index.html")
