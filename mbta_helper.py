import urllib.request
import json
from urllib.parse import quote
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "ucoV95GYWBg5FhETzJUpIKCX4AuudQkm"
MBTA_API_KEY = "b7955c38dd63454989f4451068ae9d67"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    url = f'{url}?key={MAPQUEST_API_KEY}&location=Babson%20College'
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
    loc = urllib.parse.quote(place_name)
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={loc}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    long_lat_raw = response_data['results'][0]['locations'][0]['latLng']
    
    long_lat_list = list(long_lat_raw.values())
    long_lat_tup = tuple(long_lat_list)
    # print(long_lat_tup)

    return long_lat_tup


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    # print(latitude)
    # print(longitude)
    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    f = urllib.request.urlopen(url)
    response_text2 = f.read().decode('utf-8')
    response_data2 = json.loads(response_text2)
    
    station_name = response_data2['data'][0]['attributes']['name']
    wc = response_data2['data'][0]['attributes']['wheelchair_boarding']
    if wc == 1:
        wheelchair_accessible = 'Yes'
    else:
        wheelchair_accessible = 'No'
    
    station_wc = (station_name, wheelchair_accessible)

    # print(type(station_wc))
    return station_wc


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    loc = urllib.parse.quote(place_name)
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={loc}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)

    long_lat_raw = response_data['results'][0]['locations'][0]['latLng']
    
    long_lat_list = list(long_lat_raw.values())
    long_lat_tup = tuple(long_lat_list)

    # return long_lat_tup
    latitude = long_lat_tup[0]
    longitude = long_lat_tup[1]

    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    f = urllib.request.urlopen(url)
    response_text2 = f.read().decode('utf-8')
    response_data2 = json.loads(response_text2)
    
    station_name = response_data2['data'][0]['attributes']['name']
    wc = response_data2['data'][0]['attributes']['wheelchair_boarding']
    if wc == 1:
        wheelchair_accessible = 'Yes'
    else:
        wheelchair_accessible = 'No'
    
    # station_wc = (station_name, wheelchair_accessible)

    # print(type(station_wc))
    print(f'The closest MBTA Staion is: {station_name}. Does this station have wheelchair accessbility? {wheelchair_accessible}!')


def main():
    """
    You can test all the functions here
    """
    # get_json(MAPQUEST_BASE_URL)
    # get_lat_long('South Station Boston')
    # get_nearest_station(lat, longit)
    place_name = input('Where are you? ')
    find_stop_near(place_name)

if __name__ == '__main__':
    main()