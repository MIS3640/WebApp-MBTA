import urllib.request
import urllib.parse
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# print(response_data["results"][0]["locations"][0]['postalCode'])

MBTA_BASE_URL = "https://api-v3.mbta.com/stops"
MBTA_API_KEY = "424b108e9e0442939260d4f9bf8f0685"
MAPQUEST_API_KEY =  "1zFTJI7r4ghx9tCF9Gb6H2tbkG8i0HCC"

# A little bit of scaffolding if you want to use it
# def url_encode(place):
#     '''
#     function that takes an address or place name as input and 
#     returns a properly encoded URL to make a MapQuest geocode request
#     '''
#     place = place.replace(' ', '%20')
#     params = urllib.parse.urlencode({place})
#     url = f'http://www.mapquestapi.com/geocoding/v1/address?{params}'
#     with urllib.request.urlopen(url) as f:
#         print(f.read().decode('utf-8'))
#     return url
# print(url_encode('Babson Park'))

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
    place = place_name.replace(' ', '%20')
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place}'
    place_json = get_json(url)
    return place_json['results'][0]["locations"][0]['latLng']

latLong = tuple(get_lat_long('15 Lansdowne St, Boston, MA 02215').values())
latitude = str(latLong[0])
longitude = str(latLong[1])
# print(latitude)
# print(longitude)



def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url2 = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    station_json = get_json(url2)
    return station_json['data'][0]['attributes']['name'], station_json['data'][0]['attributes']['wheelchair_boarding']
    #if wheelchair_boarding returns: 0 = no information, 1 = accessible, 2 = not accessible
# pprint(get_nearest_station(latitude, longitude))


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    get_lat_long(place_name)
    latLong = tuple(get_lat_long(place_name).values())
    latitude = str(latLong[0])
    longitude = str(latLong[1])
    return get_nearest_station(latitude, longitude)
pprint(find_stop_near('Back Bay'))


def main():
    """
    You can test all the functions here
    """
    pass


if __name__ == '__main__':
    main()
