import urllib.request
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/stops', methods=['POST', 'GET'])

def stops():
    location = request.args.get('location')
    stops = parse_json_station(location)
    return render_template('stops.html', stops=stops)


def get_geographical_data(location):
    address = location.replace(" ", "%20")
    MAPQUEST_API_KEY = "c6SEWZsdBV6fJeVO2lGbNKI1SOBgdOn3"
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={address}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def coordinates(location):
    geographical_data = get_geographical_data(location)
    total_locations = len(geographical_data['results'][0]['locations'])
    coordinate_list = []
    state = 'MA'
    for i in range(0, total_locations):
        if geographical_data['results'][0]['locations'][i]['adminArea3'] == state:
            coordinate_list.append(
                geographical_data['results'][0]['locations'][i]['displayLatLng']['lat'])
            coordinate_list.append(
                geographical_data['results'][0]['locations'][i]['displayLatLng']['lng'])
            return coordinate_list
    sys.exit('Location was invalid, try with different location.')


def get_nearest_station(location):
    coordinate_list = coordinates(location)
    latitude = coordinate_list[0]
    longitude = coordinate_list[1]
    url = f'https://api-v3.mbta.com/stops?filter[latitude]={latitude}&filter[longitude]={longitude}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def parse_json_station(location):
    station_data = get_nearest_station(location)
    if station_data['data'] == []:
        return " There Are No Close Stations"
    else:
        handicap_accessibility = station_data['data'][0]['attributes']['wheelchair_boarding']
        if handicap_accessibility == 0:
            handicap_str = 'Unsure If Handicap Accessible'
        elif handicap_accessibility == 1:
            handicap_str = 'Handicap Accessible'
        elif handicap_accessibility == 2:
            handicap_str = 'Not Handicap Accessible'
        station_name = str(station_data['data'][0]['attributes']['name'])
        final_str = station_name + ': ' + handicap_str
        return final_str


if __name__ == '__main__':
    app.run(debug=True)
