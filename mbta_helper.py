# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "6U83snPamoNXW3MWOCNJtwNnvBL6kELF"
MBTA_API_KEY = "32f72eb4c4054f0597f2d38cf50cffc0"

# A little bit of scaffolding if you want to use it
url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'

#loading the dependencies
import urllib.request
import urllib.parse
import json
from pprint import pprint

def get_formatted_url (place):
    """Write a function that takes an address or place name as input and 
    returns a properly encoded URL to make a MapQuest geocode request."""
    pass
    #USE ENCODE FUNCTION

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """

    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)

    return response_data


def get_lat_long(place_name):
    """
    #TODO: change docstring
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """

    place_name = place_name.replace(" ", "%20")
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    latLng = response_data["results"][0]["locations"][0]['latLng']
    latLng_tuple = [(k,v) for k,v in latLng.items()] #converting dict to list of tuple
    pprint(latLng_tuple)

    return latLng_tuple


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    pass


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    pass




def main():
    """
    You can test all the functions here
    """
    #Latitude and Longtitude
    print(get_lat_long("Newbury Street, Boston"))


if __name__ == '__main__':
    main()
