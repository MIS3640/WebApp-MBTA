import urllib.request
import json
from pprint import pprint


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.
    """
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
    MAPQUEST_API_KEY = 'xisuxWXkZJL4iIUV6AfIYiZtBj9rCEQQ'
    location = place_name.replace(' ', '+')
    url = 'http://www.mapquestapi.com/geocoding/v1/address?key={}&location={}'.format(MAPQUEST_API_KEY, location)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)
    place_json = get_json(url)
    lat = place_json["results"][0]["locations"][0]["latLng"]["lat"]
    lng = place_json["results"][0]["locations"][0]["latLng"]["lng"]
    return lat, lng

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    MBTA_API_KEY = '1f6d0f7abcf04b989e7d8fb5942f2ace'
    url = 'https://api-v3.mbta.com/stops?api_key={}&filter[latitude]={}&filter[longitude]={}&sort=distance'.format(MBTA_API_KEY, latitude, longitude)
    stopJson = get_json(url)
    stopName = stopJson['data'][0]['attributes']['name']

    wheelchair_accessible = stopName['data'][0]['attributes']['wheelchair_boarding']        
    if wheelchair_accessible == 1:
        print('Wheelchairs Accessible')
    elif wheelchair_accessible == 2:
        print('Wheelchairs Inaccessible')
    else:
        print("No Information Available")

    return station_name, wheelchair_accessible

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, lng = get_lat_long(place_name)
    stop_list = get_nearest_station(lat,lng)
    stop = stop_list[0]
    return (stop, distance)


def main():
    """
    You can test all the functions here
    """
    place_name = input("Please enter the location address or name:")
    print(find_stop_near(place_name))


if __name__ == '__main__':
    main()






