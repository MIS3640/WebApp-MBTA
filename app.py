from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)


@app.route("/nearest_station/", methods=["GET", "POST"])
def nearest():
    '''
    Find the nearest station.
    '''
    if request.method == "POST":
        place = request.form["Location"]
        id, station_name, wheelchair_accessible = find_stop_near(place)
 
        if station_name:
            return render_template(
                "mbta_result.html", Location = place, station_name=station_name, wheelchair_accessible=wheelchair_accessible
            )
        else: 
            return render_template('mbta_form.html', error=True)
    else:
        return render_template("mbta_form.html", error=None)
