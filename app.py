"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request, session, url_for, redirect 

from mbta_helper import find_stop_near

app = Flask(__name__)

app.secret_key = "SecretKey"

@app.route('/', methods = ['POST','GET'])

def index(): 
    """
    Home page of site
    """
    if request.method =='POST': 
        session['place'] = request.form['place']
        return redirect(url_for('nearest_mbta'))
    else: 
        return render_template('index.html')
        
@app.route('/nearest_mbta')
def nearest_mbta(): 
    """
    returns nearest mbta staion
    """
    text = find_stop_near(session['place'])
    return render_template('place.html', text = text)
