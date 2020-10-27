import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "fJZhww0hRfrdgt1UXjweedmAm9werzS3"
MBTA_API_KEY = "0088ecf73b3a47a48f1ed6733593e869"


url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'



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


# pprint(get_json(url))

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    if ' ' in place_name:
        place_name = place_name.replace(" ", "%20")
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place_name}'
    response_data = get_json(url)
    latitude = response_data["results"][0]["locations"][0]['latLng']['lat']
    longitude = response_data["results"][0]["locations"][0]['latLng']['lng']
    return (latitude, longitude)

# print(get_lat_long('Alewife Brook Parkway'))

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    response_data = get_json(url)
    station_name = response_data['data'][0]['attributes']['name']
    wheelchair = response_data['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair == 0:
        wheelchair_accessible = 'No information'
    if wheelchair == 1:
        wheelchair_accessible = 'Accessible'
    else:
        wheelchair_accessible ='Inaccessible'
    return (station_name, wheelchair_accessible)

# print(get_nearest_station(42.397122, -71.141129))


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, lng = get_lat_long(place_name)
    return get_nearest_station(lat, lng)

# print(find_stop_near('Alewife Brook Parkway'))


def main():
    """
    You can test all the functions here
    """
    pass


if __name__ == '__main__':
    main()
