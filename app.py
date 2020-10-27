from flask import Flask, render_template, request, redirect
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/nearest/', methods=['GET', 'POST'])
def nearest():
    if request.method == "POST":
        place_name = str(request.form['location name'])
        mbta_station = find_stop_near(place_name)
        station = mbta_station[0]
        wheelchair = mbta_station[1]

        if mbta_station:
            return render_template(
                "result.html", 
                place_name = place_name, 
                station = station,
                wheelchair = wheelchair
            )
        else: 
            return render_template("mbta_form.html", error = True)
    
    return render_template("mbta_form.html", error = None)

