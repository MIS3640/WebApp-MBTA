# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "reB6lcbfcK79Ksc75exZpoJHKEjE8pfS"
MBTA_API_KEY = "486c3e34aa424edbb1acefb343ae6cc6"


# A little bit of scaffolding if you want to use it
import pprint
import urllib.request
import json
url = f'http://www.mapquestapi.com/geocoding/v1/address?key=reB6lcbfcK79Ksc75exZpoJHKEjE8pfS&location=Babson%20College'
def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    with urllib.request.urlopen(url) as f:
        f = urllib.request.urlopen(url)
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        return response_data

# get_json(url)

def get_lat_long(place):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key=reB6lcbfcK79Ksc75exZpoJHKEjE8pfS&location={place}'
    d = get_json(url)
    location = d['results'][0]['locations'][0]['latLng']
    latitude = location['lat']
    longitude = location['lng']
    t = (latitude, longitude)
    return t

# print(get_lat_long('63%20Whitehead%20Avenue,%20Hull,%20MA,%2002045'))
# print(get_lat_long('Harvard%20University%20MA'))

# GPS coordinates of Babson College, United States. Latitude: 42.2923 Longitude: -71.2567

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'https://api-v3.mbta.com/stops?api_key=486c3e34aa424edbb1acefb343ae6cc6&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    response_data = get_json(url)
    # pprint.pprint(response_data)
    # id = response_data['data'][0]['id']
    try: 
        station_name = response_data['data'][0]['attributes']['name']
        wheelchair_accessible = response_data['data'][0]['attributes']['wheelchair_boarding']
        if wheelchair_accessible == 0:
            wheelchair_access = "Not wheelchair accessible"
        else:
            wheelchair_access = "Wheelchair accessible"
        return station_name, wheelchair_access
    except ValueError:
        return "Error" 
    except IndexError:
        return "Error"

print(get_nearest_station(42.2923, -71.2567))
# print(get_nearest_station(42.348457,-71.082622))
# print(get_nearest_station(42.3482677, -71.166336))

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    place_name = place_name.replace(" ", "%20")
    coordinates = get_lat_long(place_name)
    return get_nearest_station(*coordinates)
    

# start error handling here, i.e. what happens when put in babson college, and there is no result returned

# print(find_stop_near('63%20Whitehead%20Avenue,%20Hull,%20MA,%2002045'))


def main():
    """
    You can test all the functions here
    """
    address = 'Babson College'
    # location = get_lat_long(address)
    # print(get_nearest_station(*location))
    print(find_stop_near(address))

if __name__ == '__main__':
    main()

