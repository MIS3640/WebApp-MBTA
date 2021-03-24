"""
Simple "Hello, World" application using Flask
"""
import mbta_helper 
from flask import Flask
from flask import request
# from mbta_helper import find_stop_near
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/nearest/', methods=["GET", "POST"])
def get_nearest_stop():
    if request.method == "POST":
        place_name = request.form['address']
        result = mbta_helper.find_stop_near(place_name)
        if result:
            return render_template('station.html', result=result)
        else:
            return render_template("form.html", error = True)
    return render_template("error.html", error = None)
