from flask import Flask, render_template, request, url_for, flash, redirect
from mbta_helper import userlocation, fetchmap, fetchlatlng, fetchmbta

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


@app.route("/nearest/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        location = request.form["location"]
        rad = request.form["rad"]
        map_url = userlocation(location)
        response_data = fetchmap(map_url)
        latlng = fetchlatlng(response_data)
        stop_name, stop_accessible = fetchmbta(latlng, rad)
    return render_template(
        "mbta_station.html", stop_name=stop_name, stop_accessible=stop_accessible
    )


# @app.route('/nearest/', methods=["GET", "POST"])
# def search():
#     if request.method == "POST":
#         location = request.form["location"]
#         rad = request.form["rad"]
#         map_url = userlocation(location)
#         response_data = fetchmap(map_url)
#         latlng = fetchlatlng(response_data)

#         # if len(response_data[0]) == 1:
#         #     flash(u'There are no MBTA stops within {rad} miles of your location.', 'error')
#         #     return redirect(url_for('/'))
#         stop_name, stop_accessible = fetchmbta(latlng, rad)
#     return redirect(url_for('nearest_mbta', stop_name = stop_name, stop_accessible = stop_accessible))

# @app.route('/nearest_mbta/<lat>/<lng>')
# def result():
#     return render_template("mbta_station.html")
