from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/get_nearest_station/', methods=['GET', 'POST'])