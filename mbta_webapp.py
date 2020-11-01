"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("webapp.html")

@app.route("/nearest_mbta/", methods=["GET", "POST"])
def n_mbta():
    if request.method == "POST":
        pn = request.form["place_name"]
        return(find_stop_near(pn))
    else:
        return render_template("error.html")  
