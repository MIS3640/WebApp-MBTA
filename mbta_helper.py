import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MAPQUEST_API_KEY = "fr5fcfwbldhIhgGuLLYR23IBBNkl8u6k"  # got this key from https://developer.mapquest.com/

MBTA_BASE_URL_STOPS = "https://api-v3.mbta.com/stops"
MBTA_BASE_URL_SCHEDULES = "https://api-v3.mbta.com/schedules"
MBTA_API_KEY = "c195fe99627f4a2ab53642a056cd0967"  # got this key from https://api-v3.mbta.com/portal

# A little bit of scaffolding if you want to use it


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    res_text = f.read().decode("utf-8")
    res_data = json.loads(res_text)
    return res_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place_name = place_name.replace(" ", "%20")  #  to url encode
    url = f"{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place_name}"
    res_data = get_json(url)
    lat = res_data["results"][0]["locations"][0]["displayLatLng"]["lat"]
    lng = res_data["results"][0]["locations"][0]["displayLatLng"]["lng"]
    return lat, lng


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    # redius 0.02 is 1 mile. 0.01 is half mile
    url = f"{MBTA_BASE_URL_STOPS}?api_key={MBTA_API_KEY}&filter[latitude]={lat}&filter[longitude]={lng}&filter[radius]=0.02&sort=distance&page[limit]=1"
    res_data = get_json(url)
    try:
        id = res_data["data"][0]["id"]
        station_name = res_data["data"][0]["attributes"]["name"]
        code = res_data["data"][0]["attributes"]["wheelchair_boarding"]
        wheelchair_accessible = ""
        if code == 0:
            wheelchair_accessible = "No information"
        elif code == 1:
            wheelchair_accessible = "Accessible"
        elif code == 2:
            wheelchair_accessible = "Inaccessible"
    except:
        id = ""
        station_name = ""
        wheelchair_accessible = ""
    return id, station_name, wheelchair_accessible


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, lng = get_lat_long(place_name)
    id, station_name, wheelchair_accessible = get_nearest_station(lat, lng)
    return station_name, wheelchair_accessible


def main():
    """
    You can test all the functions here
    """
    lat, lon = get_lat_long("Boston Logan Airport")
    print(lat, lon)

    id, station_name, wheelchair_accesibility = get_nearest_station(lat, lon)
    print(id, station_name, wheelchair_accesibility)

    station_name, wheelchair_accessible = find_stop_near("Boston Logan Airport")
    print(station_name, wheelchair_accessible)


if __name__ == "__main__":
    main()
