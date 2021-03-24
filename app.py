"""
Simple "Hello, World" application using Flask
"""

from flask import Flask


app = Flask(__name__)


@app.route('/templates/index.html')
def hello_world():
    return 'Hello World!'
