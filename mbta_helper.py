import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "Ey0nFagbAAN4VNnTpQZg4fOpUMCOO3aG"
MBTA_API_KEY = "a1c969f6e3a641aab061eb729bf56ba0"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return(response_data)


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place_name = place_name.replace(' ', '%20')
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    response_data = get_json(url)
    long = response_data["results"][0]["locations"][0]['displayLatLng']['lng']
    lat = response_data["results"][0]["locations"][0]['displayLatLng']['lat']
    return lat, long
 


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    response_data = get_json(url)
    ID = response_data['data'][0]['id']
    station_name = response_data['data'][0]['attributes']['name']
    wheelchair_accessible = response_data['data'][0]['attributes']['wheelchair_boarding']
    return ID, station_name, wheelchair_accessible


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, long = get_lat_long(place_name)
    ID, station_name, wheelchair_accessible = get_nearest_station(lat, long)
    return ID, station_name, wheelchair_accessible


def main():
    """
    You can test all the functions here
    """
    lat, long = get_lat_long('Brookline')
    print(f'latitude:{lat}, longtitude:{long}')
    ID, station_name, wheelchair_accessible = get_nearest_station(lat, long)
    print(station_name, wheelchair_accessible)
    ID, station_name, wheelchair_accessible = find_stop_near('Brookline')


if __name__ == '__main__':
    main()