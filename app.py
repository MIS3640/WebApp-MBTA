from flask import Flask, render_template, request
import mbta_helper

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def index():
    map_key, search_key = mbta_helper.get_keys()
    try:
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
                map_key=map_key,
                search_key=search_key,
            )
        return render_template(
            "index.html",
            place_name=False,
            lat=42.3601,
            lng=-71.0589,
            map_key=map_key,
            search_key=search_key,
        )
    except:
        return render_template("error.html")


@app.route("/error")
def error():
    return render_template("error.html")