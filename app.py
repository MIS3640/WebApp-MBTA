"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import request
from flask import render_template
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/nearest_mbta/", methods=["POST"])
def find():
    try:
        loc = str(request.form["location"])
        station_name, wheelchair_accessibility = find_stop_near(loc)
    except:
        return render_template("result.html", error=True)

    if station_name:  # returns result page
        return render_template(
            "result.html",
            location=loc,
            station_name=station_name,
            wheelchair_accessibility=wheelchair_accessibility,
        )
    else:  # returns error info
        return render_template("result.html", error=True)
