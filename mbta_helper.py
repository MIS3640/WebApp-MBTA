import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
# MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
# MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# # Your API KEYS (you need to use your own keys - very long random characters)
# MAPQUEST_API_KEY = "2bvJCZ8VpUKoqpSZXDD6NfXjsaKsLH1q"
# MBTA_API_KEY = "177043a1f6ac4a44ab3d765eff40d67a"


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
    MAPQUEST_API_KEY = "2bvJCZ8VpUKoqpSZXDD6NfXjsaKsLH1q"
    d = {'location':place_name}
    result = urllib.parse.urlencode(d)
    url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&{result}"
    json = get_json(url)
    lat = json["results"][0]["locations"][0]["latLng"]["lat"]
    lng = json["results"][0]["locations"][0]["latLng"]["lng"]
    return (lat, lng)


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    MBTA_API_KEY = "177043a1f6ac4a44ab3d765eff40d67a"
    d = {'latitude': latitude, 'longitude':longitude}
    result = urllib.parse.urlencode(d)
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&{result}"
    json = get_json(url)
    try:
        station_name = json['data'][0]['attributes']['name']
        wheelchair_accessible  = json['data'][0]['attributes']['wheelchair_boarding']
        return (station_name, wheelchair_accessible)
    except IndexError:
        return 1
    


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat_long = get_lat_long(place_name)
    station_wheelchair = get_nearest_station(*lat_long)
    if station_wheelchair == 1: 
        return "No stations nearby"
    if station_wheelchair[1] == 0: 
        return f'The nearest station is {station_wheelchair[0]} and there is no info on wheelchair accessibility'
    elif station_wheelchair[1] == 1: 
        return f'The nearest station is {station_wheelchair[0]} and there is wheelchair accessibility'
    elif station_wheelchair[1] == 2: 
        return f'The nearest station is {station_wheelchair[0]} and there is no wheelchair accessibility'

def main():
    """
    You can test all the functions here
    """
    # MAPQUEST_API_KEY = "2bvJCZ8VpUKoqpSZXDD6NfXjsaKsLH1q"
    # url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=wellesley'
    # pprint(get_json(url))
    # test = get_lat_long('Boston College')
    # print(test)
    # print(get_nearest_station(*test))
    print(find_stop_near('Wellesley'))

if __name__ == '__main__':
    main()
