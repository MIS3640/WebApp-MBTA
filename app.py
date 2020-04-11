from flask import Flask, render_template, request, redirect, url_for, session
from main import read_url, get_lag, get_lng, get_nearest_station, run_all

app = Flask(__name__)
app.secret_key = 'sddfklsdhdjkASKLFDHJrfDSFRPdf'

@app.route('/',methods=['POST','GET'])
def index():
    '''
    main page that greets the users and takes a text input of location
    '''

    if request.method =='POST':
        place = request.form["nm"]
        session['place'] = place
        return redirect(url_for("place"))
    else:
        return render_template('index.html')



@app.route('/nearest')
def place():
    '''
    the output page that shows the outcome message
    shows an error page when the location input is invalid
    '''
    try:
        if "place" in session:
            place = session["place"]
            # where_you_are = input('Please tell me your current location>>>  ')
            # data=read_url(place) 
            # # print(get_lag(data))
            # # print(get_lng(data))
            # latitude = get_lag(data)
            # longitude = get_lng(data)
            # print(f'<h1>Yout starting location is: {place}</h1>')
            # return (f'<h1>{get_nearest_station(latitude,longitude)}</h1>')
            # return f'<h1>{place}</h1>'
            return (f'<h1>{run_all(place)}</h1>')
        else: 
            return redirect(url_for("/"))
    except IndexError:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)