import json
from pprint import pprint
import urllib.request

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
# MAPQUEST_API_KEY = "mMcQPxMFW14DpNaZOkv18VNaRYk2zw48"
# MBTA_API_KEY = "eac51a1891444d13a851327a6e301ab5"

# A little bit of scaffolding if you want to use it

with open("sensitive.txt", "r") as handle:
    data = handle.read()

config = json.loads(data)
MAPQUEST_API_KEY = config["MAPQUEST_API_KEY"]
MBTA_API_KEY = config["MBTA_API_KEY"]
PLACE_SEARCH_KEY = config["PLACE_SEARCH_KEY"]


def get_keys():
    return (MAPQUEST_API_KEY, PLACE_SEARCH_KEY)


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    # pprint(response_data)
    return response_data


def replace_spaces(location_str):
    new_location = location_str.replace(" ", "%20")
    return new_location


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    print(f"SEARCHING FOR: {place_name}")
    place_name = replace_spaces(place_name)
    url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}"
    r = get_json(url)
    pprint(r)
    if len(r["results"]) > 0:
        lat = r["results"][0]["locations"][0]["latLng"]["lat"]
        lng = r["results"][0]["locations"][0]["latLng"]["lng"]
        print(f"latitude is: {lat}, longitude is {lng}")
        return (lat, lng)
    return (42.3601, -71.0589)


def get_nearest_station(latitude, longitude, distance, wheelchair_required):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    distance = distance * 0.02
    print(f"Distance is {distance}")
    url = f"https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}&filter%5Bradius%5D={distance}"
    r = get_json(url)
    stops = r["data"]
    # pprint(r)
    if len(r["data"]) == 0:
        return ("No stops nearby", "No stops to check")
    else:
        if wheelchair_required:
            for stop in stops:
                stop_name = stop["attributes"]["name"]
                wheelchair_accessible = stop["attributes"]["wheelchair_boarding"]
                if wheelchair_accessible == 1:
                    return (stop_name, "Yes")
            return ("No stops found", "No stops to check")

        stop_name = stops[0]["attributes"]["name"]
        wheelchair_accessible = stops[0]["attributes"]["wheelchair_boarding"]
        if wheelchair_accessible == 0:
            wheelchair_accessible = "Unknown"
        elif wheelchair_accessible == 1:
            wheelchair_accessible = "Yes"
        else:
            wheelchair_accessible = "No"
        return (stop_name, wheelchair_accessible)


def find_stop_near(place_name, distance, wheelchair_required):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, lng = get_lat_long(place_name)
    print(wheelchair_required)
    if wheelchair_required == "true":
        return get_nearest_station(lat, lng, distance, True)
    return get_nearest_station(lat, lng, distance, False)


def main():
    """
    You can test all the functions here
    """
    print(find_stop_near("Boston", 1, "true"))


if __name__ == "__main__":
    main()
