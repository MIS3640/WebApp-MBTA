# Useful URLs (you need to add the appropriate parameters for your requests)
import json
import sys
import urllib.request
from pprint import pprint

MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "c6SEWZsdBV6fJeVO2lGbNKI1SOBgdOn3"
MBTA_API_KEY = "da74e2e522c444b8b3aa624b39aa5a2a"


def locate_address():
    """This function takes the users current location and then formats it so that if there are any spaces, 
    it changes it to %20. This makes it so that it can be used with a URL"""
    location = str(input("What is your current location? "))
    location = location.replace(' ', '%20')
    return location


def get_geographical_data():
    """This function locates the address that the user inputs and runs it
     through the api in order to get the geographical data of the input"""
    address = locate_address()
    MAPQUEST_API_KEY = "c6SEWZsdBV6fJeVO2lGbNKI1SOBgdOn3"
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={address}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def coordinates():
    """This function parses through the json package in order to just look at the first location 
    and then extracts that locations longitude and latitude.
    If the location is invalid, the code will respond saying so. """
    geographical_data = get_geographical_data()
    total_locations = len(geographical_data['results'][0]['locations'])
    coordinate_list = []
    state = 'MA'
    for i in range(0, total_locations):
        if geographical_data['results'][0]['locations'][i]['adminArea3'] == state:
            coordinate_list.append(
                geographical_data['results'][0]['locations'][i]['displayLatLng']['lat'])
            coordinate_list.append(
                geographical_data['results'][0]['locations'][i]['displayLatLng']['lng'])
            return coordinate_list
    sys.exit('Location was invalid, try with different location.')


def get_nearest_station():
    """This function uses the previous function to find the nearest station 
    to the longitutde and latitude coordinates found in the json package."""
    coordinate_list = coordinates()
    latitude = coordinate_list[0]
    longitude = coordinate_list[1]
    url = f'https://api-v3.mbta.com/stops?filter[latitude]={latitude}&filter[longitude]={longitude}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def parse_json_station():
    """This function also uses the previous function in order to find the station closest to the 
    users coordinates and also tells the user if the MBTA station has handicap accessibility. """
    station_data = get_nearest_station()
    if station_data['data'] == []:
        return "There Are No Close Stations"
    else:
        handicap_accessibility = station_data['data'][0]['attributes']['wheelchair_boarding']
        if handicap_accessibility == 0:
            handicap_str = 'Unsure if Handicap Accessible'
        elif handicap_accessibility == 1:
            handicap_str = 'Handicap Accessible'
        elif handicap_accessibility == 2:
            handicap_str = 'Not Handicap Accessible'
        station_name = str(station_data['data'][0]['attributes']['name'])
        final_str = station_name + ': ' + handicap_str
        return final_str


if __name__ == '__main__':
    parse_json_station()
