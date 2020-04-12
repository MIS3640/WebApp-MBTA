"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, StringField, validators
from mbta_helper import find_stop_near

app = Flask(__name__)

class MbtaForm(Form):
    """
    Represents a form that requires a user's input of a location or address.
    """
    placename = StringField('Please enter a location or address:', [validators.DataRequired()])

@app.route('/')
def home_page():
    """
    Returns a template that renders the home page with the MBTA form. 
    """
    form = MbtaForm(request.form)
    return render_template('index.html', form=form)
    
@app.route('/nearest', methods=['POST'])
def find_nearest_stops():
    """
    Takes in the form with the user's input. 
    If the form is valid, redirect the request to the handler for finding the nearest MBTA stop.
    Otherwise, render the home page with the form with errors. 
    """
    form = MbtaForm(request.form)
    if form.validate():
        return redirect(url_for('find_nearest_mbta_stop'), code=307)
    else:
        return render_template('index.html', form=form)

@app.route('/nearest_mbta', methods=['POST'])
def find_nearest_mbta_stop():
    """
    Takes in a form with a field for a place name, and tries to find the closest MBTA stop. 
    If such MBTA stop exists, return template that renders a page with the stop name and if it's wheelchair accessible.
    Otherwise, return template that renders an error page with a link to the home page.
    """
    place_name = request.form.get('placename')
    try:
        stop_name, is_wheelchair_accessible = find_stop_near(place_name)
        print(stop_name, is_wheelchair_accessible)
        return render_template('nearest_mbta.html', stop_name=stop_name, wheelchair_accessible=is_wheelchair_accessible)
    except:
        return render_template('error.html')
