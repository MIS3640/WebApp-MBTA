import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "oclty3rBpodkIo8cppeUJ4R3NVJNYVXd"
MBTA_API_KEY = "de38bca41be64ad3963d0e604007c984"


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


def get_lat_lng(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place_name = place_name.replace(' ', '%20')
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    response_data = get_json(url)
    lat = response_data["results"][0]["locations"][0]['displayLatLng']['lat']
    lng = response_data["results"][0]["locations"][0]['displayLatLng']['lng']
    return lat, lng


def get_nearest_station(lat, lng):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={lat}&filter[longitude]={lng}&filter[radius]=0.02&sort=distance&page[limit]=1'
    response_data = get_json(url)
    station_name, wheelchair_accessible = response_data['data'][0]['attributes']['name'], response_data['data'][0]['attributes']['wheelchair_boarding']

    return station_name, wheelchair_accessible

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, lng = get_lat_lng(place_name)
    station_name, wheelchair_accessible = get_nearest_station(lat, lng)
    return station_name, wheelchair_accessible

def main():
    """
    You can test all the functions here
    """
    # lat, lng = get_lat_lng('Cleveland Circle')
    # print(f'latitude:{lat}, longtitude:{lng}')
    # station_name, wheelchair_accesible = get_nearest_station(lat, lng)
    # print(station_name, wheelchair_accesible)
    print(find_stop_near('Cleveland Circle'))

if __name__ == '__main__':
    main()
