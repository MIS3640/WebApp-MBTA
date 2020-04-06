import urllib.request
import urllib.parse
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = f'http://www.mapquestapi.com/geocoding/v1/address?'
MBTA_BASE_URL = 'https://api-v3.mbta.com/stops'

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = 'JNVOQp6Yig9sib6RVBnpbBpbirMOzyG1'
MBTA_API_KEY = "d657ba4068af473bb42cff137b163785"


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
    params = {'key': MAPQUEST_API_KEY, 'location': place_name}
    a = urllib.parse.urlencode(params)
    url = MAPQUEST_BASE_URL +str(a)
    response_data = get_json(url)
    pprint(response_data)
    locLen = 0  # sections counts the number of locations
    for x in (response_data["results"][0]["locations"]):
        locLen = locLen + 1
    count = 0
    if locLen ==0: print("No location found.")
    elif locLen ==1:  #condition when one location comes up thats not MA
        if response_data["results"][0]["locations"][0]["adminArea3"] != 'MA':
            print("ERROR: MA LOCATION NOT FOUND")
            exit() # exits code because you can't do anything
    else: #when there is more than one location
        while(count != locLen-1):
            if response_data["results"][0]["locations"][count]["adminArea3"] == 'MA':
                break
            else:
                count = count + 1
        if response_data["results"][0]["locations"][count]["adminArea3"] != 'MA': # exists if last loc is not MA
            print("ERROR: MA LOCATION NOT FOUND.")
            exit()
    return response_data["results"][0]["locations"][count]["displayLatLng"]


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'https://api-v3.mbta.com/stops?api_key=9d7fbfd56c164a2bbedb3691a1a79949&filter%5Blatitude%5D='\
          +str(latitude)+'&filter%5Blongitude%5D='\
          +str(longitude)
    response_data = get_json(url)
    #pprint(response_data) # ! THIS IS TO LIST OUT ALL OF THE LOCATIONS
    if response_data["data"] == []:
        print("No stops nearby")
        exit()
    return response_data["data"][0]["attributes"]


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat_long_tuple = get_lat_long(place_name)
    lat = lat_long_tuple['lat']
    long = lat_long_tuple['lng']
    #print('OUR COORDINATES ARE' + str(lat) + ' ' + str(lng)) #! THIS IS TO RECORD THE LAT LONG OF INPUT LOCATION
    response_data = get_nearest_station(lat, long)
    print(response_data["name"])
    if response_data["wheelchair_boarding"] == 0:
        print("No information on wheelchair boarding")
    elif response_data["wheelchair_boarding"] == 1:
        print("	Accessible (if trip is wheelchair accessible)")
    else:
        print("Inacessible")


def main():
    """
    You can test all the functions here
    """
    find_stop_near("129 Tremont St, Boston, MA 02108")

if __name__ == '__main__':
    main()