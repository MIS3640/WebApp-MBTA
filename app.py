# SQLite Reference: https://www.youtube.com/watch?v=Z1RJmh_OqeA

from flask import Flask, render_template, request, url_for, redirect
from mbta_helper import find_stop_near
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    current_location = db.Column(db.String(200),nullable=False)
    nearest_mbta = db.Column(db.String(200), nullable=False)
    accessibility = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Profile %r>' % self.id  
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name= None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)


@app.route("/nearest_station/", methods=["GET", "POST"])
def nearest():
    '''
    Find the nearest station.
    '''
    if request.method == "POST":
        place = request.form["Location"]
        id, station_name, wheelchair_accessible = find_stop_near(place)
        new_profile = Profile(current_location=id, nearest_mbta = station_name, accessibility=wheelchair_accessible)

        try:
            db.session.add(new_profile)
            db.session.commit()
            return render_template(
                "mbta_result.html", Location = place, station_name=station_name, wheelchair_accessible=wheelchair_accessible
            )
        except:
            return "There was an issue adding your location"
    
        if station_name:
            createprofile()
            return render_template(
                "mbta_result.html", Location = place, station_name=station_name, wheelchair_accessible=wheelchair_accessible
            )
        else: 
            return render_template('mbta_form.html', error=True)
    else:
        profile = Profile.query.order_by(Profile.date_created).all()
        return render_template("mbta_form.html", error=None)
