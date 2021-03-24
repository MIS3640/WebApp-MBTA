import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)

MAPQUEST_API_KEY = "BuiFO4y1yA2XdShQy6sqQ247sDePMMdL"
MBTA_API_KEY = "0e4429dd66af42f09a95defce173911f"

# A little bit of scaffolding if you want to use it

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
    place = place_name.replace(' ', '%20')
    url = '{}?key={}&location={}'.format(MAPQUEST_BASE_URL, MAPQUEST_API_KEY, place) # access map quest
    print(url)
    place_json = get_json(url)
    lat = place_json['results'][0]['locations'][0]['latLng']['lat'] # pulls latitude from JSON results
    lon = place_json['results'][0]['locations'][0]['latLng']['lng'] # Longitude
    print(lat, lon)
    return lat, lon

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = '{}?api_key={}&filter[latitude]={}&filter[longitude]={}&sort=distance'.format(MBTA_BASE_URL, MBTA_API_KEY, latitude, longitude) # use cordinants from 
    print(url)
    station_json = get_json(url) # url from MBTA, to pull station
    print(station_json)
    station_name = station_json['data'][0]['attributes']['name'] # nearest station name
    print(station_name)
    wheelchair_accessible = station_json['data'][0]['attributes']['wheelchair_boarding'] # pulls wheelchair discription from JSON
    return station_name, wheelchair_accessible
    
    
def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    return get_nearest_station(*get_lat_long(place_name)) # return to tie it all together. 

