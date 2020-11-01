"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import *


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method != "POST":
            return render_template('index.html', error=None)
        elif request.method == "POST":
            location = request.form["location"]
            nearest = find_stop_near(location)
            if nearest:
                return render_template('nearest_station.html', location=location, nearest=nearest)
    except:
        return render_template('error.html')

