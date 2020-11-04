
# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from mbta_helper import *

# create the application object
app = Flask(__name__)

# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    location = None
    wheelChairAcessibility = None
    if request.method == 'POST':
        if 'submit_a' in request.form:
            return render_template('index.html', error=error, location=location, wheelChairAcessibility=wheelChairAcessibility)
        if request.form['city'] != None and request.form['max'] != None:
            city = request.form['city']
            maxDistance = request.form['max']
            stationDetails = getStationInformation(city, maxDistance)
            if stationDetails != None:
                location = stationDetails[1]
                wheelChairAcessibility = stationDetails[0]
                return render_template('resultsPage.html', location=location, wheelChairAcessibility=wheelChairAcessibility)
            else:
                error = "no stops found in range :("
                return redirect(url_for('error'))
        else:
            error = "Please fill out all fields"
            return redirect(url_for('error'))
    elif request.method == 'GET': 
        return render_template('index.html', error=error, location=location, wheelChairAcessibility=wheelChairAcessibility)

@app.route('/nearest_mbta', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        return redirect(url_for('login'))
    elif request.method == 'GET':
        return(render_template('resultsPage.html'))

@app.route('/error', methods=['GET', 'POST'])
def error():
    if request.method == 'POST':
        return redirect(url_for('login'))
    elif request.method == 'GET':
        return(render_template('error.html'))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)