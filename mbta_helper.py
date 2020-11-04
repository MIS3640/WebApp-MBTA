import requests
import json
from pprint import pprint
import urllib
from math import sqrt

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "YloRmEG0nfFqrQdarRGsdvp7cAQnPpFH"
MBTA_API_KEY = "3f400aec85814677adfe52868e7b6b38"
 
# A little bit of scaffolding if you want to use it
def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """ 
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    data = json.loads(response_text)
    return data

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    data = get_json(url)
    latitudeLongitude = data["results"][0]["locations"][0]["latLng"]
    lat = latitudeLongitude['lat']
    lng = latitudeLongitude['lng']
    return lat, lng


def get_information_about_station(closestStop):
    """
    Given closest stop, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'https://api-v3.mbta.com/stops?filter[id]={closestStop}'
    stop_data = get_json(url)
    wheelchairAccessibility = stop_data['data'][0]['attributes']['wheelchair_boarding']
    stopName = stop_data['data'][0]['attributes']['name']
    if wheelchairAccessibility == 0:
        wheelchairAccessibility = 'No wheelchair information is avaliable'
    elif wheelchairAccessibility == 1:
        wheelchairAccessibility = 'The station is wheelchair accessible'
    elif wheelchairAccessibility == 2:
        wheelchairAccessibility = 'The station is not accessible to wheelchairs'
    information = (wheelchairAccessibility, stopName) 
    return information


def find_stop_near(place_name, maxDistanceToTravel):
    #for max distance to travel, 0.02 = 1 mile
    lat, lng = get_lat_long(place_name)
    #using these as sample values for now 
    #lat, lng = 43.392097, -71.004818
    url = f'https://api-v3.mbta.com/stops?filter[latitude]={lat}&filter[longitude]={lng}&filter[radius]={maxDistanceToTravel}'
    mbta_data = get_json(url)
    #access the first element of the mbta_data class
    shortestDistance = 360
    closestStop = None
    for i in mbta_data['data']:
        #iterate over all of the bus stops within range, then use the distance formula to see which ones are closest
        lati = i['attributes']['latitude']
        longi  = i['attributes']['longitude']
        distanceToStop = sqrt(pow((lati-lat), 2)+pow((longi-lng), 2))
        if distanceToStop < shortestDistance:
            shortestDistance = distanceToStop
            #gives us the id for use later
            closestStop = i['id']

    return shortestDistance, closestStop

def getStationInformation(cityName, MaxDistance):
    """
    enter city name and the maximum distance you are willing to travel, 
    then return wheelchair acessibility and the name of the stop
    """
    try:
        shortestDistance, closestStop = find_stop_near(cityName, MaxDistance)
    #print(closestStop)
        if closestStop != None:
            stationDetails = get_information_about_station(closestStop)
            return stationDetails
        else:
            print('No stop in specified range was found :(')
            return None
    except:
        print('Please double check the values entered')
        return None

def main():
    """
    You can test all the functions here
    """
    city = input('city name')
    maxDistance = input('max distance')
    stationDetails = getStationInformation(city, maxDistance)


if __name__ == '__main__':
    main()
