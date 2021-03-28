from flask import Flask, render_template, redirect, request
from forms import GeoForm
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Ctreate the index page of the website requesting place name from user and returns the information about 
    the closet MBTA station and wheelchair accessibility for the station"""
    # print(request.form)
    form = GeoForm(request.form)
    if form.validate(): 
        place_name = request.form.get('placename')
        print('placename:', place_name)
        (station, wheelchair_accessible) = find_stop_near(place_name)
        print('station:', station)
        print('wheelchair_accessible:', wheelchair_accessible)

        return render_template('mbta.html',
                place_name = place_name,
                station = station,
                wheelchair_accessible = wheelchair_accessible)

    return render_template('index.html', form=form)


@app.route('/test', methods=['GET'])
def test(): 
    """create test page for the mbta.html"""
    place_name = 'boston'
    station =  'ABC'
    wheelchair_accessible = 'Accessible'
    return render_template('mbta.html',
            place_name = place_name,
            station = station,
            wheelchair_accessible = wheelchair_accessible)

@app.route('/test_empty', methods=['GET'])
def test_empty(): 
    """create test page for the mbta.html"""
    place_name = 'boston'
    station =  ''
    wheelchair_accessible = ''
    return render_template('mbta.html',
            place_name = place_name,
            station = station,
            wheelchair_accessible = wheelchair_accessible)

if __name__ == "__main__":
    app.run(debug=True)
