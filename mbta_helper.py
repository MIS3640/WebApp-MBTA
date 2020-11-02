import urllib.request
import urllib.parse
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "o9zmlFPBkUTrYdgeYOLGGMwI2N22hhzw"
MBTA_API_KEY = "15205bbf7f744225b638708280d528f9"


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

    request_url = map_quest_request_url(place_name)
    try:
        json_data = get_json(request_url)
        lat = json_data["results"][0]["locations"][0]["latLng"]["lat"]
        lng = json_data["results"][0]["locations"][0]["latLng"]["lng"]
        lat_lng = (lat, lng)
        return lat_lng

    except:
        print("Error when fetching lat lng information")
        raise Exception


def map_quest_request_url(place_name):
    params = urllib.parse.urlencode({'key': MAPQUEST_API_KEY, 'location': place_name})
    request_url = MAPQUEST_BASE_URL + "?" + params
    return request_url

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    request_url = mbta_request_url(latitude, longitude)

    # Add api key to request header
    req = urllib.request.Request(
        request_url,
        headers={"x-api-key": MBTA_API_KEY}
    )

    f = urllib.request.urlopen(req)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    if len(response_data["data"]) > 0:
        nearest_stop = response_data["data"][0]["attributes"]

        wheelchair_info = {
            0: "No information",
            1: "Accessible",
            2: "Inaccessible"
        }

        result_tuple = (nearest_stop["name"], wheelchair_info[nearest_stop["wheelchair_boarding"]])
        return result_tuple

    return "No nearest MBTA stop found", "No information"


def mbta_request_url(latitude, longitude):
    params = urllib.parse.urlencode({
        'sort': 'distance',
        'filter[latitude]': latitude,
        'filter[longitude]': longitude,
    })
    request_url = MBTA_BASE_URL + "?" + params
    return request_url


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    try:
        lat_lng = get_lat_long(place_name)
        nearest_stop = get_nearest_station(lat_lng[0], lat_lng[1])
        return nearest_stop
    except:
        print("Error when fetching nearest stops")
        raise Exception


def main():
    """
    You can test all the functions here
    """
    place_name = "30 Leggs Hill Road, Marblehead, MA 01945 Marblehead Massachusetts United States"
    place_name = "150 Humphrey Street, Marblehead, MA 01945 Marblehead Massachusetts United States"
    lat_lng = get_lat_long(place_name)
    # get_nearest_station(42.489729, -70.892)
    get_nearest_station(lat_lng[0], lat_lng[1])


if __name__ == '__main__':
    main()


