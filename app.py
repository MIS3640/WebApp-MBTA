from flask import Flask, render_template, request

from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        try:
            place_name = request.form['name']
            city = request.form['city']
            state = request.form['state']
            place = place_name + ',' + city + ',' + state

            station_name, wheelchair_accessible = find_stop_near(place_name)
            print(station_name, wheelchair_accessible)
            
            if wheelchair_accessible:
                return render_template('result.html', place_name=place, station_name=station_name, wheelchair_accessible="")
            
            else:
                return render_template('result.html', place_name=place, station_name=station_name, wheelchair_accessible="Not")
        except:
            return render_template('hello.html', error=True)
    return render_template('hello.html', error=None)
   