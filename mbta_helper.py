# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "TBDo2JHjPzxATo89WX0IaKybW0VRYtvf"
MBTA_API_KEY = "62eb3f8d91fe4bf3bc54d56c4d194cd8"

# A little bit of scaffolding if you want to use it

import urllib.request
import json
from pprint import pprint

API_KEY = ""
Location = ""


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
    address = place_name.strip()
    response_data = get_json(
        f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={address}"
    )
    coordinates = response_data["results"][0]["locations"][0]["displayLatLng"]
    tup1 = coordinates.items()
    print(tup1)


# lat': 42.296927,'lng': -71.291858
get_lat_long("Wellesley")


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    f1 = urllib.request.urlopen(
        MBTA_BASE_URL + f"/data/" + {index} + f"/attributes/{latitude}"
    )
    response_text1 = f.read().decode("utf-8")
    latitude = json.loads(response_text)

    f2 = urllib.request.urlopen(
        MBTA_BASE_URL + f"/data/" + {index} + f"/attributes/{latitude}"
    )
    response_text2 = f.read().decode("utf-8")
    longitude = json.loads(response_text) / data / {index} / attributes / longitude


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    f1=urllib.request.urlopen("https://api-v3.mbta.com/stops")
    text=f1.read().decode("utf-8")
    stops=json.loads(text)
    print(type(stops))
    print(stops.keys())
    for element in stops["data"]:
        if element["attributes"]["municipality"]==place_name:
            name=element["attributes"]["name"]
            wheelchair_access=element['attributes']['wheelchair_boarding']
    
    return name, wheelchair_access



def main():
    """
    You can test all the functions here
    """
    name, access=find_stop_near("Wellesley")
    print(name, access)


if __name__ == "__main__":
    main()
