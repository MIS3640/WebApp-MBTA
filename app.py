"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import request
from mbta_helper import find_stop_near

app = Flask(__name__)


# @app.route('/templates/index.html')
# @app.route(POST/nearest)
# def hello_world():
#     return 'Hello World!'

@app.route('/templates/index.html', methods=['POST'])
def mbta_stop():
    # error = None
    try:
        if request.method == 'POST':
            place_name = request.form['address']
            station_name, wheelchair_access = find_stop_near(place_name)
            return station_name, wheelchair_access
    except:
        print('hello')