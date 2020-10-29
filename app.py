from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/MBTA/", methods=["GET", "POST"])
def response():
    if request.method == "POST":
        place_name = request.form["Place Name"]
        city = request.form["City"]
        name = find_stop_near(place_name, city)
        if name:
            return render_template(
                "response.html", place_name=place_name, city=city, name=name
            )
    else:
        return render_template("index.html", error=True)
    return render_template("index.html", error=None)
