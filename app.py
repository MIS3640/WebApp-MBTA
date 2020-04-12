from flask import Flask, render_template, request, url_for
from mbta_helper import find_stop_near
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class History(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.String(200),nullable=False)
    mbta = db.Column(db.String(200), nullable=False)
    accessible= db.Column(db.String(200), nullable=False)
    time = db.Column(db.DateTime, default = datetime.utcnow)
    def __repr__(self):
        return '<History %r>' % self.id  


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)


@app.route("/Closest MBTA Station/", methods=["GET", "POST"])
def station():
    '''
    Identify the closest station.
    '''
    if request.method == "POST":
        place = request.form["Location"]
        ID, station_name, wheelchair_accessible = find_stop_near(place)
        history = History(location=id, mbta = station_name, accessible=wheelchair_accessible)

        try:
            db.session.add(history)
            db.session.commit()
            return render_template(
                "mbtaresult.html", Location = place, station_name=station_name, wheelchair_accessible=wheelchair_accessible
            )
        except:
            return "There was an issue adding your location"

        if station_name:
            return render_template(
                "mbtaresult.html", Location = place, station_name=station_name, wheelchair_accessible=wheelchair_accessible)
        else: 
            return render_template('mbtaform.html', error=True)
    else:
        history = History.query.order_by(History.date_created).all()
        return render_template("mbtaform.html", error=None)