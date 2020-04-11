from flask import Flask
from flask import request
from flask import render_template
from mbta_helper import find_stop_near, get_schedule


app = Flask(__name__)


@app.route('/')
def index():
    ''' home page '''
    return render_template('index.html')

@app.route('/nearest_MBTA/', methods=['GET', 'POST'])
def find():
    ''' find nearest MBTA function '''
    if request.method == 'POST':
        # get location information
        try:
            place = str(request.form['Location'])
            id, station_name, wheelchair_Accessibility = find_stop_near(place)
        except:
            return render_template('form.html', empty=True)

        # get extra information requirements
        try:
            extra_info1 = str(request.form['extra_info1'])
        except:
            extra_info1 = ''
        try:
            extra_info2 = str(request.form['extra_info2'])
        except:
            extra_info2 = ''
        try:
            limit = int(request.form['schedule number'])
        except:
            limit = 1

        # check if user needs any extra information, get arrival time if schedule is required
        wheelchair = False
        schedule = False
        arrival = ''

        if 'wheelchair' in extra_info1:
            wheelchair = True
        if 'schedule' in extra_info2:
            schedule = True
            try:
                arrival = ', '.join(get_schedule(id, limit))
            except:
                arrival = 'not available'

        # returns result page 
        if station_name:
            return render_template('result.html', 
            Location=place, station_name=station_name, wheelchair_Accessibility=wheelchair_Accessibility, arrival=arrival,
            wheelchair=wheelchair, schedule=schedule)
        # returns error if there's no station near by
        else:
            return render_template('form.html', error=True)
    return render_template('form.html', error=False)