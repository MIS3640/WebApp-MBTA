"""
A MBTA helper application using Flask that helps users find
the nearest MBTA station near them.
"""

from flask import Flask
from flask import request
from flask import render_template
import mbta_helper

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def welcome():
    return render_template("welcome.html")

@app.route("/nearest", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        place_name = request.form.get("place_name")
        radius = request.form.get("radius")
        route_type = request.form.get("route_type")
        station_name, wheelchair_accessibility = mbta_helper.find_stop_near(place_name, radius,route_type)
        return render_template("results.html", station_name=station_name,
                               wheelchair_accessibility=wheelchair_accessibility, radius = radius, route_type = route_type)
    return render_template("welcome.html")



if __name__ == "__main__":
    app.run(debug=True)

