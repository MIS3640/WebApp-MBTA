"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/hello_world/')
def hello_world():
    return render_template('webapp.html')

print(hello_world())
