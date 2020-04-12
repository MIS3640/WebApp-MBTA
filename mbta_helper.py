import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "M7wyf4gSK6OmzjgcfbnkrzpKlKjLgknO"
MBTA_API_KEY = "ba051b07c46f4b2191bd16ae02fa5929"

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
    place_name = place_name.replace(" ", "%20") + ",%20Boston,%20MA" # Formats inputted street address
    latLng = get_json(f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}")["results"][0]["locations"][0]["latLng"]
    if latLng["lat"] == 42.52277 and latLng["lng"] == -70.91888: # Due to l33 "%20Boston,%20MA", this latLng is returned even with garbage input
        return "n/a", "n/a"
    else:
        return latLng["lat"], latLng["lng"]

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    response_data = get_json(f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance")["data"][0]['attributes']
    return response_data["name"], response_data["wheelchair_boarding"]

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    response_data = get_nearest_station(get_lat_long(place_name)[0], get_lat_long(place_name)[1])
    if response_data[1] == 0:
        accessible_info = "unknown whether it is accessible"
    elif response_data[1] == 1:
        accessible_info = "accessible"
    elif response_data[1] == 2:
        accessible_info = "inaccessible"
    return f"The nearest station to {place_name} is {response_data[0]}, and it is {accessible_info} via wheelchair"

def main():
    pass

if __name__ == '__main__':
    main()