"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request, url_for

from mbta_helper import *


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def mbta_helper():
    if request.method == 'POST':
        location = str(request.form['location'])
        MBTA_station, wheelchair_accesibility = find_stop_near(location)
        print(MBTA_station, wheelchair_accesibility)
        if MBTA_station:
            return render_template(
               'result.html', location=location, MBTA_station=MBTA_station, wheelchair_accesibility=wheelchair_accesibility
            )
        else:
            return render_template('index.html', error=True)
    return render_template('index.html', error=None)
