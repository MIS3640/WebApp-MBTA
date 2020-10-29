from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def response():
    if request.method == "POST":
        place_name = request.form["Place Name"]
        city = request.form["City"]
        response = find_stop_near(place_name, city)
        if response == "No Nearby Stops":
            return render_template("index.html", error=True)
        else:
            return render_template(
                "response.html", place_name=place_name, city=city, name=response
            )
    return render_template("index.html", error=None)
