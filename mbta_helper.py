import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "eTPA7RkuW1uYnRpsbHBtdxhub5hpi1iw"
MBTA_API_KEY = "72ac95663fb5416780be51b329261101"


# A little bit of scaffolding if you want to use it


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    return response_data


# url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
# pprint(get_json(url))


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place_name = str.replace(place_name, " ", "%20")
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    response_data = get_json(url)
    d = response_data["results"][0]["locations"][0]["latLng"]
    return d

# print(get_lat_long("58 Boylston Street Malden MA"))


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    output = get_json(url)
    if output["data"][0]["attributes"]["wheelchair_boarding"]== 1:
        return f'The closest stop is: {output["data"][0]["attributes"]["name"]} and it is Wheelchair Accessible'
    else:
        return f'The closest stop is: {output["data"][0]["attributes"]["name"]} and it is NOT Wheelchair Accessible'
# get_lat_long("58 Boylston Street Malden MA")
# print(get_nearest_station(42.422741, -71.056043))

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    d = get_lat_long(place_name)
    latitude = float(d['lat'])
    longitude = float(d['lng'])
    output = get_nearest_station(latitude, longitude)
    return output

# print(find_stop_near('Babson College'))

def main():
    """
    You can test all the functions here
    """
    print(find_stop_near('58 Boylston Street Malden MA'))


if __name__ == "__main__":
    main()
