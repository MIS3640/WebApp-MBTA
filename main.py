import urllib.request
import json
from pprint import pprint
# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "XbNTIQMhKz0tClvI7KVdJnGxdwp9Esvu"
MBTA_API_KEY = "ebcc79c2c7dc44d5b6f012325e8692d1"


def read_url(place_name):
    """
    takes an address or place name as input 
    returns a properly encoded URL to make a MapQuest geocode request
    """
    locate = place_name.replace(' ','%20')
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={locate}'
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        # pprint(response_data)
        return(response_data)
        # print(response_data["results"][0]["locations"][0]['postalCode'])

def get_lag(source):
    """
    extract the latitude from JSON response
    """
    lag = source['results'][0]['locations'][0]['displayLatLng']['lat']
    return(lag)

def get_lng(source):
    """
    extract the longitude from JSON response
    """
    lng = source['results'][0]['locations'][0]['displayLatLng']['lng']
    return(lng)

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        # pprint(response_data)
        station_name = response_data['data'][0]['attributes']['name']
        accessible = response_data['data'][0]['attributes']['wheelchair_boarding']
        if accessible == 0:
            return(f'The cloest station from this location is {station_name}, but there lacks info on accessibility for this stop.')
        elif accessible == 1:
            return(f'The cloest station from this location is {station_name}, and this station is wheelchair friendly.')
        elif accessible ==2:
            return(f'The cloest station from this location is {station_name}, but this station is NOT wheelchair friendly.')
        else: 
            return('error')

        
    # with urllib.request.urlopen(url) as f:
    #     response_text = f.read().decode('utf-8')
    #     data = json.loads(response_text)
    #     return pprint(data) 
        

def run_all(place):
    '''
    to be used together with app.py
    take place name and return nearest stop and accessibility of the stop
    '''
    data=read_url(place) 
    # print(get_lag(data))
    # print(get_lng(data))
    latitude = get_lag(data)
    longitude = get_lng(data)
    # print(f'Yout starting location is: {where_you_are}')
    result = get_nearest_station(latitude,longitude)
    return result 

def main():
    where_you_are = input('Please tell me your current location>>>  ')
    data=read_url(where_you_are) 
    # print(get_lag(data))
    # print(get_lng(data))
    latitude = get_lag(data)
    longitude = get_lng(data)
    print(f'Yout starting location is: {where_you_are}')
    print(get_nearest_station(latitude,longitude))

if __name__ == '__main__':
    main()

