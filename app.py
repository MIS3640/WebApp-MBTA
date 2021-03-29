"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from part1 import get_address, lat_long, mbta

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def mbta_helper():
    if request.method == "POST":
        address = request.form["address"]
        info = mbta(address)

        if info:
            name, wheelchair = info
            return render_template(
                "mbta_result.html",
                name = name,
                wheels = wheelchair
            )
        else:
            return render_template("index.html", error = True)
    return render_template("index.html", error = None)   

if __name__ == "__main__":
    app.run(debug=True)