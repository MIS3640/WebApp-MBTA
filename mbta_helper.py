# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "bvd5kR5ANCpY295vIH5qgDEcpKZzeuKR"
MBTA_API_KEY = "250359d96859421394c2f37d6c25e26d"


# A little bit of scaffolding if you want to use it

import json
import urllib.request
from pprint import pprint


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place_name = place_name.replace(" ", "%20")

    latLng = get_json(f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}")["results"][0]["locations"][0]["latLng"]

    return latLng["lat"], latLng["lng"]

#print(get_lat_long('Harvard'))

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    #using Boston address as place holder in below url1
    url1 =  'https://api-v3.mbta.com//stops?api_key=250359d96859421394c2f37d6c25e26d&filter[latitude]=42.352975&filter[longitude]=-71.055560&sort=distance'
    f = urllib.request.urlopen(url1)
    response_text1 = f.read().decode('utf-8')
    response_data1= json.loads(response_text1)
    stopName = (response_data1['data'][0]["attributes"]['name'])
    wheelchair_accessible = (response_data1['data'][0]["attributes"]['wheelchair_boarding'])
    if wheelchair_accessible == 1: 
        print('It\'s wheelchair accessible')
    else: 
        print('it is not wheelchair accessible')
    return (stopName)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    response_data2 = get_nearest_station(get_lat_long(place_name)[0], get_lat_long(place_name)[1])
    print(response_data2)


#find_stop_near('Harvard')

def main():
    """
    You can test all the functions here
    """
    pass


if __name__ == '__main__':
    main()
