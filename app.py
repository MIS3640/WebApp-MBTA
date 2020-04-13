from flask import Flask, render_template, request, redirect, url_for, session
from mbta_helper import find_stop_near

app = Flask(__name__)

app.secret_key = "theworldsmostsecretkey" # Secret Key required for session["place"] to store info


@app.route('/',methods=['POST','GET'])
def home():
    """ 
        Home page of the website
    """
    if request.method =='POST':
        session["place"] = request.form["place"] # store "place" input
        return redirect(url_for("nearest"))
    else:
        return render_template("index.html")


@app.route("/nearest")
def nearest():
    """ 
        Returns any nearby MTBA stations if possible
    """
    try:
        text = find_stop_near(session["place"])
        return render_template("place.html", text = text)
    except:
        return render_template('error.html')
