""" 
1. Upon visiting the index page at `http://127.0.0.1:5000/`, the user will be greeted by a page that says hello, and includes an input **form** that requests a place name.
2. Upon clicking the 'Submit' button, the data from the form will be sent via a POST request to the Flask backend at the route `POST /nearest`
3. (Optional) Perform some simple validation on the user input. See [wtforms](https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/).
4. The Flask backend will handle the request to `POST /nearest_mbta`. Then your app will render a `mbta_station` page for the user - presenting nearest MBTA stop and whether it is wheelchair accessible. In this step, you need to use the code from Part 1.
5. If something is wrong, the app will render a simple error page, which will include some indication that the search did not work, in addition to a button (or link) that will redirect the user back to the home page.
"""
from flask import Flask, render_template, request, url_for, flash, redirect
from mbta_helper import userlocation, fetchmap, fetchlatlng, fetchmbta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/nearest/', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        location = request.form["location"]
        rad = request.form["rad"]
        map_url = userlocation(location)
        response_data = fetchmap(map_url)
        latlng = fetchlatlng(response_data) 

        # if len(response_data[0]) == 1:
        #     flash(u'There are no MBTA stops within {rad} miles of your location.', 'error')
        #     return redirect(url_for('/'))
        stop_name, stop_accessible = fetchmbta(latlng, rad)
    return redirect(url_for('nearest_mbta', stop_name = stop_name, stop_accessible = stop_accessible))

@app.route('/nearest_mbta/')
def result():
    return render_template("mbta_station.html")



# @app.route('/nearest/', methods=["GET", "POST"])
# def search():
#     if request.method == "POST":
#         location = request.form["location"]
#         rad = request.form["rad"]
#         map_url = userlocation(location)
#         response_data = fetchmap(map_url)
#         latlng = fetchlatlng(response_data) 
#         stop_name, stop_accessible = fetchmbta(latlng, rad)
#     return render_template("mbta_station.html", stop_name = stop_name, stop_accessible = stop_accessible)

    
    
    
