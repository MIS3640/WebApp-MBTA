from flask import Flask, request, render_template
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/nearest_MBTA/", methods=["POST", "GET"])
def find():
    if request.method == "POST":

        try:  # get information about user's location
            user_location = request.form.get(
                "location"
            )  # gets location from the user and stores it in a variable
            station_name, wheelchair_accessibility = find_stop_near(
                user_location
            )  # uses the user input in the 'find_stop_near' function and returns output
        except:
            return render_template("error.html", empty=True)

        if station_name:  # displays the result page
            return render_template(
                "result.html",
                user_location=user_location,
                station_name=station_name,
                wheelchair_accessibility=wheelchair_accessibility,
            )
        else:  # displays the error page
            return render_template("error.html", error=True)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
