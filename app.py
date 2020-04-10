from flask import Flask
from flask import request
from flask import render_template
from mbta_helper import find_stop_near, get_schedule


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nearest_MBTA/', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        place = str(request.form['Location'])
        id, station_name, wheelchair_Accessibility = find_stop_near(place)
        try:
            arrival = ', '.join(get_schedule(id))
        except:
            arrival = 'not available'

        try:
            extra_info1 = str(request.form['extra_info1'])
        except:
            extra_info1 = ''
        try:
            extra_info2 = str(request.form['extra_info2'])
        except:
            extra_info2 = ''
    
        wheelchair = False
        schedule = False

        if 'wheelchair' in extra_info1:
            wheelchair = True
        if 'schedule' in extra_info2:
            schedule = True
        
        if station_name:
            return render_template('result.html', 
            Location=place, station_name=station_name, wheelchair_Accessibility=wheelchair_Accessibility, arrival=arrival,
            wheelchair=wheelchair, schedule=schedule)
        else:
            return render_template('form.html', error=True)
    return render_template('form.html', error=False)