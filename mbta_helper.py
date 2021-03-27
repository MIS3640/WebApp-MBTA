# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "GKbhF2b2TZvZ9AAGw5d9s8YipmSAFvXk"
MBTA_API_KEY = "7f92e7087bd34f2c9e29a0c40646ad50"


# A little bit of scaffolding if you want to use it

import json
import urllib.request
import urllib.parse
import pprint

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    url = MAPQUEST_BASE_URL + "?" + urllib.parse.urlencode({"key":MAPQUEST_API_KEY, "location":place_name})
    # pprint.pprint(get_json(url))
    LatLng = get_json(url)["results"][0]["locations"][0]["displayLatLng"]
    lat = LatLng["lat"]
    lng = LatLng["lng"]
    return lat, lng


def get_nearest_station(position):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = MBTA_BASE_URL + "?" + urllib.parse.urlencode({"api_key":MBTA_API_KEY,"filter[latitude]": position[0], "filter[longitude]": position[1], "filter[radius]": 0.02*5}) #filter[route_type]': route_type})
    station_name = get_json(url)["data"][0]["attributes"]["name"]
    wheelchair = get_json(url)['data'][0]['attributes']['wheelchair_boarding']
    if not wheelchair or wheelchair == 0: 
        wheelchair_accessible = "No accessibility information for the trip."
    elif wheelchair == 1:
        wheelchair_accessible = "Vehicle being used on this particular trip can accommodate at least one rider in a wheelchair."
    elif wheelchair == 2:
        wheelchair_accessible = "No riders in wheelchairs can be accommodated on this trip."
    return station_name, wheelchair_accessible


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and 
    whether it is wheelchair accessible.
    """
    latitude = get_lat_long(place_name)[0]
    longtitude = get_lat_long(place_name)[1]
    position = (latitude,longtitude)
    return get_nearest_station(position)


def main():
    """
    You can test all the functions here
    """
    # print(get_lat_long("Allston"))
    # print(get_nearest_station(get_lat_long("Allston")))
    print(find_stop_near("231 Forest Street, Babson Park, MA"))


if __name__ == '__main__':
    main()



