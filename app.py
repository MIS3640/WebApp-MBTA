from flask import Flask, render_template, request
from mbta_helper import find_stop_near
from the_map import find

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def theLocation():
    if request.method == 'POST':
        place_name = request.form["location"]
        stop, wheelchair_boarding = find_stop_near(place_name)
        return render_template("result.html", stop=stop, wheelchair= wheelchair_boarding)
    else:
        return render_template("index.html")