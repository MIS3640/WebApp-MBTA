from flask import Flask, render_template, request
import mbta_helper

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        place_name = request.form["place_name"]
        distance = int(request.form["distance"])
        wheelchair_required = request.form["wheelchair"]
        lat, lng = mbta_helper.get_lat_long(place_name)
        stop_name, wheelchair = mbta_helper.find_stop_near(
            place_name, distance, wheelchair_required
        )
        return render_template(
            "index.html",
            place_name=place_name,
            stop_name=stop_name,
            wheelchair=wheelchair,
            lat=lat,
            lng=lng,
        )
    return render_template("index.html", place_name=False, lat=42.3601, lng=-71.0589)


# WHAT THE APP SHOULD DO:
# User can select a Dunkin' on the map
# Pop-up will come up with some of the things around it/some stats about the dunks
# If you click get MBTA directions, it will show you how to get to the Dunkin' using the MBTA
