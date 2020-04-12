import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "https://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "JLP0dYNyUhZXHbTzv2vzs4s3XHJbBlk9"
MBTA_API_KEY = "c1af34d3361b4e5a8140a22fbe55b989"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    print("Getting {}".format(url))
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return response_data

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    params = {
        'key': MAPQUEST_API_KEY, 
        'location': place_name 
    }
    encoded_params = urllib.parse.urlencode(params)
    url = MAPQUEST_BASE_URL +  '?'  + encoded_params
    data = get_json(url)
    lat_long = data.get('results')[0].get('locations')[0].get('latLng')
    return (lat_long.get('lat'), lat_long.get('lng'))

def get_nearest_stop(latitude, longitude):
    """
    Given latitude and longitude strings, return a (stop_name, wheelchair_accessible)
    tuple for the nearest MBTA stop to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    params = {
        'api_key': MBTA_API_KEY,
        'filter[latitude]': latitude, 
        'filter[longitude]': longitude,
        'filter[radius]': 20,
        'sort': 'distance',
        'page[limit]': 1
    }
    encoded_params = urllib.parse.urlencode(params)
    url = MBTA_BASE_URL + '?' + encoded_params
    data = get_json(url)

    closest_stop = data.get('data')[0]
    attributes = closest_stop.get('attributes')
    return (attributes.get('name'), attributes.get('wheelchair_boarding') == 1)

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, long = get_lat_long(place_name)
    stop_name, wheelchair_accessible = get_nearest_stop(str(lat), str(long))
    print("Closest stop is: {}".format(stop_name))
    if wheelchair_accessible:
        print("stop is wheelchair accessible")
    else:
        print("Stop is not wheelchair accessible")
    
    return (stop_name, wheelchair_accessible)

def main():
    """
    You can test all the functions here
    """
    place_name = input('Enter a place or address:\n')
    find_stop_near(place_name)

if __name__ == '__main__':
    main()
