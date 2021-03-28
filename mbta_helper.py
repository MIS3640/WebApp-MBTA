import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
# MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
# MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "UpEbLghM3a0HX7d7VYARwKPaKrAm2nGH"
MBTA_API_KEY = "87dc928cdb404ae48c5c1aa1213c4ac8"


def buildUrl(place_name):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    params = urllib.parse.urlencode({"key": MAPQUEST_API_KEY, "location": place_name})
    url = "http://www.mapquestapi.com/geocoding/v1/address?%s" % params
    return url


def get_lat_long(res):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    data = res["results"][0]["locations"][0]["displayLatLng"]
    return data["lat"], data["lng"]


def get_closed_stop(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    This functio will return a (latitude, longitude, station name, wheelchair_accessible),
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    
    """
    

    url = buildUrl(place_name)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    # pprint(response_data)

    lat, lng = get_lat_long(response_data)

    # test for MBTA stop
    params = urllib.parse.urlencode(
        {
            "sort": "distance",
            "filter[latitude]": lat,
            "filter[longitude]": lng,
            "filter[radius]": 0.1,
        }
    )

    url = "https://api-v3.mbta.com/stops?%s" % params
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)

    if len(response_data["data"]) == 0:
        return lat, lng, None, None

    print(response_data["data"][0])

    name = response_data["data"][0]["attributes"]["name"]
    wheelchair_boarding = response_data["data"][0]["attributes"]["wheelchair_boarding"]

    return lat, lng, name, wheelchair_boarding


def main():
    """
    You can test all the functions here
    """
    # print(lat)
    # print(lng)
    # pprint(response_data)
    # print(name)
    # print(wheelchair_boarding)
    pass


if __name__ == "__main__":
    main()
