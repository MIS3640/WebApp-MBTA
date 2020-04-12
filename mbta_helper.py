import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "usx5AjPsMDXCpwlQcnIp6mJ9HAnNxuNx"
MBTA_API_KEY = "4800dbf6194442a08871582e4d62887d"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    MAPQUEST_API_KEY = "usx5AjPsMDXCpwlQcnIp6mJ9HAnNxuNx"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place_name}'
    place_response_data = get_json(url)

    latitude = place_response_data['results'][0]['locations'][0]['latLng']['lat']
    longitude = place_response_data['results'][0]['locations'][0]['latLng']['lng']
    return latitude, longitude
   

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    station_response_data = get_json(url)

    station = station_response_data['data'][0]['attributes']['name']
    wheelchair = station_response_data['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair == 1:
        wheelchair = 'Accessible'
    elif wheelchair == 2:
        wheelchair = 'Inaccessbile'
    else:
        wheelchair = 'No information'
    return station, wheelchair


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    latitude, longitude = get_lat_long(place_name)
    return get_nearest_station(latitude, longitude)


def main():
    """
    You can test all the functions here
    """
    location = input('Enter the name of your location:')
    # print(get_lat_long(location))
    print(find_stop_near(location))


if __name__ == '__main__':
    main()
