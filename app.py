from flask import render_template, Flask, request, redirect
import requests  # used requests package instead because it is bettter
import json
import math


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/nearest', methods=['GET', 'POST'])
def get_userlocation():
    if request.method == 'POST':
        location = request.form['address']
    # initialize by passing location onto Mapquest API
    MAPQUEST_API_KEY = 'wiGyI5fgWUoyGvlIFDarRqZwDSAD4Aoj'
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location}'
    response_text = requests.get(url)
    response_data = response_text.json()
    # get latitude and longitude of the location
    lat = response_data["results"][0]["locations"][0]['displayLatLng']['lat']
    lng = response_data["results"][0]["locations"][0]['displayLatLng']['lng']
    latlng = [lat, lng]
    longitude = latlng[1]
    latitude = latlng[0]
    # Create a nested list of the MBTA stops closest to the latitude and longitude of the location
    url = f'https://api-v3.mbta.com/stops/?filter[latitude]={latitude}&filter[longitude]={longitude}'
    response_text = requests.get(url)
    response_data = response_text.json()
    stoplatlng = []
    for i in range(len(response_data['data'])):
        if response_data['data'][i]['attributes']['vehicle_type'] == 1:
            stoplatlng.append([response_data['data'][i]['attributes']['latitude'],
                               response_data['data'][i]['attributes']['longitude']])
    # create a list of the distances between the MBTA stop and the location
    distance = []
    for i in range(len(stoplatlng)):
        dist = math.sqrt(
            ((latitude - stoplatlng[i][0]) ** 2) + ((longitude - stoplatlng[i][1]) ** 2))
        distance.append(dist)
    # identify which distance in the distance list is the shortest
    shortest_distance = distance[0]
    for dist in distance:
        if dist < shortest_distance:
            shortest_distance = dist
    # find the index of the shortest distance and trace this index back to the stoplatlng list to find the closest MBTA stop
    index = 0
    for i in range(len(distance)):
        if shortest_distance == distance[i]:
            break
        else:
            index += 1
    shortest_distancelatlng = stoplatlng[index]
    latitude = shortest_distancelatlng[0]
    longitude = shortest_distancelatlng[1]
    # get station name and whether it is wheelchair accessible
    for i in range(len(response_data['data'])):
        if response_data['data'][i]['attributes']['latitude'] == latitude and response_data['data'][i]['attributes']['longitude'] == longitude:
            station = response_data['data'][i]['attributes']['name']
            if response_data['data'][i]['attributes']['wheelchair_boarding'] == 1:
                return render_template('nearest.html', station=station, explanation='There is wheelchair boarding')
            else:
                return render_template('nearest.html', station=station, explanation='No wheelchair boarding')
            break


@app.errorhandler(Exception)
# handles all exceptions
def error404(error):
    return render_template('error.html', explanation='The address you entered could not be found')
