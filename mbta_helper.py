import urllib.request
import json
from pprint import pprint
import urllib.request
import urllib.parse


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "1n2jcreY3jYHR3OY9YuCqFTIuFDlt2lB"
MBTA_API_KEY = "f09faa734172472e83084ecb5ceb31a5"


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
    params = urllib.parse.urlencode(
        {'key': MAPQUEST_API_KEY, 'location': place_name})
    url = MAPQUEST_BASE_URL + "?" + params
    LatLng = get_json(url)["results"][0]["locations"][0]['displayLatLng']
    return LatLng['lat'], LatLng['lng']


def get_nearest_station(latitude, longitude, route_type):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    params = urllib.parse.urlencode(
        {'api_key':MBTA_API_KEY,'filter[latitude]': latitude, 'filter[longitude]': longitude, 'filter[route_type]': route_type})
    url = MBTA_BASE_URL + "?" + params
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    station_name = response_data['data'][0]['attributes']['name']
    wheelchair_boarding = response_data['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair_boarding == 0:
        wheelchair_accessible = "No Information"
    elif wheelchair_boarding == 1:
        wheelchair_accessible = "Accessible (if trip is wheelchair accessible)"
    elif wheelchair_boarding == 2:
        wheelchair_accessible = "Inaccessible"
    return station_name, wheelchair_accessible
    
def realtime_arrival(station_name,route_type):
    params = urllib.parse.urlencode({'filter[stop]':station_name,'filter[route_type]':route_type})
    url = "https://api-v3.mbta.com/predictions?" + params
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

def find_stop_near(place_name, route_type):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    latitude = get_lat_long(place_name)[0]
    longtitude = get_lat_long(place_name)[1]
    return get_nearest_station(latitude, longtitude, route_type)


def main():
    """
    You can test all the functions here
    """
    print(find_stop_near('Jamaica Plain, MA, 02130', 1))
    # print(realtime_arrival(find_stop_near('Jamaica Plain, MA, 02130', 1)[0],1))


if __name__ == '__main__':
    main()
