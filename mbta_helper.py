import urllib.request
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "3ARDm5kXCkY7rY52SF9XIWduvdRGV2v9"
MBTA_API_KEY = "6f281f79382041de9dcdf84dac7e73a3"

# A little bit of scaffolding if you want to use it

# def get_json(url):
#     """
#     Given a properly formatted URL for a JSON web API request, return
#     a Python JSON object containing the response to that request.
#     """
#     url = f''http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}''
#     f = urllib.request.urlopen(url)
#     response_text = f.read().decode('utf-8')
#     response_data = json.loads(response_text)
#     pprint(response_data)
#     return(response_data["results"][0]["locations"][0]['postalCode'])

# print(get_json(url))


def get_lat_long(location):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)
    results = response_data['results'][0]['locations'][0]['latLng']
    latitude = results.get('lat')
    longitude = results.get('lng')
    return(latitude, longitude)

#print(get_lat_long('Boston,MA'))


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&page[limit]=1&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)
    results = response_data['data'][0]['attributes']
    whc = results.get('wheelchair_boarding')
    if whc == 0:
        whcr = "Wheelchair Access: No Information"
    elif whc == 1:
        whcr = "Wheelchair Accessible"
    else:
        whcr = "Wheelchair Inaccessible"      
    nme = results.get('name')
    clstation = (nme, whcr)
    return clstation

#print(get_nearest_station("42.358894", "-71.056742"))

def find_stop_near(location):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat_long = get_lat_long(location)
    latitude = lat_long[0]
    print(latitude)
    longitude = lat_long[1]
    print(longitude)
    return get_nearest_station(latitude, longitude)
    

print(find_stop_near('Wellesley,MA'))

# def main():
#     """
#     You can test all the functions here
#     """
#     pass


# if __name__ == '__main__':
#     main()
