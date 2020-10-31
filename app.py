"""
Amazing app to help you find nearest MBTA station
"""

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import session
from mbta_helper import find_stop_near

app = Flask(__name__)

app.secret_key = 'ilovepython'


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/nearest', methods=['POST'])
def form():
    if request.method == 'POST':
        place_name = request.form['place_name']
        route_type = request.form['route_type']
        try:
            station_name, wheelchair_accessibility = find_stop_near(
                place_name, route_type)
            session['station_name'] = station_name
            session['wheelchair_accessibility'] = wheelchair_accessibility
            return redirect(url_for('result'))
        except:
            return render_template('mbta_error.html')


@app.route('/nearest_mbta', methods=['GET', 'POST'])
def result():
    if request.method == "GET":
        station_name = session.get("station_name")
        wheelchair_accessibility = session.get("wheelchair_accessibility")

        return render_template("mbta_station.html", station_name=station_name,
                               wheelchair_accessibility=wheelchair_accessibility)
