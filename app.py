from flask import Flask, render_template, request

from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)


@app.route("/locator/", methods=["GET", "POST"])
def near_station():
    if request.method == "POST":
        place_name = str(request.form["place name"])
        near_stop = find_stop_near(place_name)
        stop = near_stop[0]
        wheelchair = near_stop[1]

        if near_stop:
            return render_template(
                "station_result.html", place_name=place_name, stop=stop, wheelchair=wheelchair
            )
        else:
            return render_template("station_form.html", error=True)
    return render_template("station_form.html", error=None)