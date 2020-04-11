"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flast import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
