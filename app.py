"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import request
from mbta_helper import find_stop_near
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/nearest', methods=["POST"])
def get_nearest_stop():
    place_name = request.form['address']
    return render_template('station.html', nearest_stop=nearest_stop)

@app.route('/backToHome', methods=["POST"])
def back_to_home():
    return redirect(url_for('main_page'))










# @app.route('/templates/index.html', methods=['POST'])
# def mbta_stop():
#     # error = None
#     try:
#         if request.method == 'POST':
#             place_name = request.form['address']
#             station_name, wheelchair_access = find_stop_near(place_name)
#             return station_name, wheelchair_access
#     except:
#         print('hello')