from flask import Flask, render_template, request
from mbta_helper import find_stop_near, get_schedule, get_distance

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def indext():
    if request.method == "POST":
        location = str(request.form["location"])
        stop = find_stop_near(location)[0]
        acc = find_stop_near(location)[1]
        if acc == 1:
            acc = "Yes"
        elif acc == 2:
            acc = "No"
        else:
            acc = "Unknown"
        schedule = get_schedule(location)
        distance = get_distance(location)

        if stop:
            return render_template(
                "nearest.html", 
                location = location, 
                stop = stop,
                acc = acc,
                schedule = schedule,
                distance = distance 
            )
        else:
            return render_template(
                "index.html",
                error = True
            )
    return render_template(
        "index.html",
        error = None
    )