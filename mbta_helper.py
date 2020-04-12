# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "xisuxWXkZJL4iIUV6AfIYiZtBj9rCEQQ"
MBTA_API_KEY = "1f6d0f7abcf04b989e7d8fb5942f2ace"

import urllib.request
import json
from pprint import pprint

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    MAPQUEST_API_KEY = 'xisuxWXkZJL4iIUV6AfIYiZtBj9rCEQQ'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    url2 = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location}'
    f = urllib.request.urlopen(url2)
    response_text2 = f.read().decode('utf-8')
    response_data2 = json.loads(response_text)
    latLong = (response_data2["results"][0]["locations"][0]["postalCode"])
    print('The Latitude Is: ',latLong.get("lat"))
    print('The Longitude Is: ',latLong.get("lng"))

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    MBTA_API_KEY = '1f6d0f7abcf04b989e7d8fb5942f2ace'
    latitude = latLong.get('lat')
    longitude = latLong.get('lng')
    url3 = 'https://api-v3.mbta.com/stops?api_key={}&filter[latitude]={}&filter[longitude]={}&sort=distance'.format(MBTA_API_KEY, latitude, longitude)
    y = urllib.request.urlopen(url3)
    response_text3 = y.read().decode('utf-8')
    response_data_3 = json.loads(response_text2)
    stopName = (response_data_3['data'][0]["attributes"]['name'])
    wheelchair_accessible = (response_data_3['data'][0]["attributes"]['wheelchair_boarding'])
    print('The Closest Stop To You is: ',stopName)
    
def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    if wheelchair_accessible == 1:
        print('Wheelchairs Accessible')
    elif wheelchair_accessible == 2:
        print('Wheelchairs Inaccessible')
    else:
        print("No Information Found")

def main():
    """
    You can test all the functions here
    """
    location = input('Please the location:')
    print(get_lat_long(location))
    print(find_stop_near(location))

if __name__ == '__main__':
    main()






