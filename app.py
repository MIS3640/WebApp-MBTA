from flask import Flask, render_template, request, url_for
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
# def index1():
#     return render_template("index.html")


def close_stop():
    if request.method == "POST":
        place_name = request.form["location"]
        mbtastation = find_stop_near(place_name)
        station_name = mbtastation[0]
        wheelchair_accesibility = mbtastation[1]
        # station_name, wheelchair_accessible = find_stop_near(place_name)

        if mbtastation:
            return render_template(
                "result.html",
                place_name=place_name,
                station_name=station_name,
                wheelchair_accesibility=wheelchair_accesibility,
            )
        else:
            return render_template("index.html", error=True)
    return render_template("index.html", error=None)