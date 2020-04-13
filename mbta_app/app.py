import json

from flask import Flask, request, render_template, redirect, url_for
import mbta_helper
from mbta_helper import WheelchairBoarding


app = Flask(__name__, static_url_path='/static', )


@app.route("/")
def index():
    error: bool = request.args.get("not_found")
    error_message: str = "No stop was found for the address provided."
    return render_template("index.html", error=error, error_message=error_message)


@app.route("/nearest_mbta/", methods=["GET", "POST"])
def nearest_mbta():
    if request.method == "POST":
        address = request.form["address"]
        try:
            stop = mbta_helper.find_nearest_stop(address)
            if stop["wheelchair_boarding"] == WheelchairBoarding.accessible:
                accessibility = stop["name"] + " is accessible."
            elif stop["wheelchair_boarding"] == WheelchairBoarding.inaccessible:
                accessibility = stop["name"] + " is inaccessible."
            else:
                accessibility = "There is no information about accessibility"
            google_maps = mbta_helper.google_maps(stop['latitude'], stop['longitude'])
            street_view = mbta_helper.street_view(stop['latitude'], stop['longitude'])
            return render_template("stop.html", stop=stop, accessibility=accessibility, google_maps=google_maps,
                                   street_view=street_view)
        except mbta_helper.StopNotFoundError:
            return redirect(url_for('index', not_found=True))
    else:
        return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
