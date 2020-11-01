import requests 
from pprint import pprint

from datetime import datetime
from pytz import timezone

import geopy.distance

def get_json(url):
    """
    url: string

    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    return requests.get(url).json()
    
    
def get_lat_long(location):
    """
    location: string

    Given a place name or address, return a (latitude, longitude) tuple for the coordinates
    """
    mapquest_api_key = "zkc3hXSnY8AXa3xnJ6P3GTKp0qi6SnIr"
    mapquest_base_url = "http://www.mapquestapi.com/geocoding/v1/address?"

    url = f'{mapquest_base_url}key={mapquest_api_key}&location={location}'

    response = get_json(url)['results'][0]['locations'][0]['latLng']
    return (response['lat'], response['lng'])


def get_nearest_station(latitude, longitude):
    """
    latitude, longtitude: string

    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station
    """
    mbta_api_key = "10575b002aae4dfab95e62c80f1c5f35"
    mbta_base_url = "https://api-v3.mbta.com/stops?"

    url = f'{mbta_base_url}api_key={mbta_api_key}&filter[latitude]={latitude}&filter[longitude]={longitude}&page[limit]=1&sort=distance'

    response = requests.get(url).json()['data'][0]
    return response
    


def find_stop_near(location):
    """
    location: string

    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    response = get_nearest_station(*get_lat_long(location))['attributes']
    return (response['name'], response['wheelchair_boarding'])


def get_schedule(location):
    '''
    location: string

    Give a place name or address, return list of upcoming shcedule for the nearest MBTA stop
    '''
    mbta_api_key = "10575b002aae4dfab95e62c80f1c5f35"
    mbta_base_url = "https://api-v3.mbta.com/schedules?"
    time = datetime.now(timezone('EST')).strftime('%H:%M')
    stop = get_nearest_station(*get_lat_long(location))['id']

    url = f'{mbta_base_url}api_key={mbta_api_key}&fields[schedule]=departure_time&filter[stop]={stop}&filter[min_time]={time}&sort=departure_time'

    response = requests.get(url).json()['data']
    schedule = []

    for item in response:
        schedule.append(item['attributes']['departure_time'][11:16])

    return schedule


def get_distance(location):
    '''
    location: string

    Give a place name or adress, return distance between the location and closest MBTA stops
    '''
    start = get_lat_long(location)
    stop = get_nearest_station(*get_lat_long(location))['attributes']
    end = (stop['latitude'], stop['longitude'])

    return f'{round(geopy.distance.distance(start, end).km, 2)} km'


def main():
    """
    You can test all the functions here
    """
    location = 'Boston University, MA'
    print(find_stop_near(location))
    print(get_schedule(location))
    print(get_distance(location))




if __name__ == '__main__':
    main()
