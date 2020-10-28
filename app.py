"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import request
from flask import render_template
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def hello():
    if request.method == 'POST':
        place_name = request.form['place_name']
        route_type = request.form['route_type']
        try:
            station_name, wheelchair_accessibility = find_stop_near(place_name, route_type)
            return render_template("mbta_station.html", station_name=station_name, wheelchair_accessibility=wheelchair_accessibility)
        except:
            return render_template('mbta_error.html')
    return render_template('index.html')



