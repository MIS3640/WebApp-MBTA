import urllib.request
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL_STOPS = "https://api-v3.mbta.com/stops"
MBTA_BASE_URL_SCHEDULES = "https://api-v3.mbta.com/schedules"


# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "oclty3rBpodkIo8cppeUJ4R3NVJNYVXd"
MBTA_API_KEY = "de38bca41be64ad3963d0e604007c984"


# A little bit of scaffolding if you want to use it

def get_json(url):
    ''' Given a properly formatted URL for a JSON web API request, 
    return a Python JSON object containing the response to that request.
    '''
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

def get_lat_lng(place_name):
    ''' Given a place name or address, 
    return a (latitude, longitude) tuple with the coordinates of the given place.
    '''
    place_name = place_name.replace(' ', '%20')
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    response_data = get_json(url)
    lat = response_data["results"][0]["locations"][0]['displayLatLng']['lat']
    lng = response_data["results"][0]["locations"][0]['displayLatLng']['lng']
    return lat, lng

def get_nearest_station(lat, lng):
    ''' Given latitude and longitude strings, return a (id, station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    '''
    url = f'{MBTA_BASE_URL_STOPS}?api_key={MBTA_API_KEY}&filter[latitude]={lat}&filter[longitude]={lng}&filter[radius]=0.02&sort=distance&page[limit]=1'
    response_data = get_json(url)
    try:
        id = response_data['data'][0]['id']
        station_name = response_data['data'][0]['attributes']['name']
        wheelchair_code = response_data['data'][0]['attributes']['wheelchair_boarding']
        wheelchair_accessible = wheelchair_accesibility(wheelchair_code)
    except:
        id = ''
        station_name = ''
        wheelchair_accessible = ''
 
    return id, station_name, wheelchair_accessible

def get_schedule(id, limit=1):
    ''' Given id of a station and limit (default to 1), 
    return an next arrival times list for the corresponding MBTA station
    id: string
    limit: integer, number of next arrival times to return
    '''
    url = f'{MBTA_BASE_URL_SCHEDULES}?api_key={MBTA_API_KEY}&filter[stop]={id}&sort=arrival_time&page[limit]={limit}'
    response_data = get_json(url)
    time = []
    for i in range(limit):
        time.append(response_data['data'][i]['attributes']['arrival_time'])

    arrival = arrival_time(time)
    return arrival

def arrival_time(time_list):
    ''' formats the arrival time response data from MBTA API
    '''
    for i, time in enumerate(time_list):
        time_list[i] = time[:19].replace('T', ' ')

    return time_list

def wheelchair_accesibility(code):
    ''' returns the corresponding meaning of the wheelchair_accesibility response data from the MBTA API
    '''
    if code == 0:
        return 'No information'
    elif code == 1:
        return 'Accessible'
    elif code == 2:
        return 'Inaccessible'

def find_stop_near(place_name):
    ''' Given a place name or address, 
    return the id and name of the nearest MBTA stop and whether it is wheelchair accessible.
    '''
    lat, lng = get_lat_lng(place_name)
    id, station_name, wheelchair_accessible = get_nearest_station(lat, lng)
    return id, station_name, wheelchair_accessible

def main():
    """
    You can test all the functions here
    """
    # lat, lng = get_lat_lng('Cleveland Circle')
    # print(f'latitude:{lat}, longtitude:{lng}')
    # id, station_name, platform, wheelchair_accessible = get_nearest_station(lat, lng)
    # print(station_name, wheelchair_accessible)

    # url = f'{MBTA_BASE_URL_STOPS}?api_key={MBTA_API_KEY}&filter[latitude]={lat}&filter[longitude]={lng}&filter[radius]=0.02&sort=distance&page[limit]=1'
    # response_data = get_json(url)

    # pprint(response_data)

    id, station_name, wheelchair_accessible = find_stop_near('Cleveland Circle')
    arrival = get_schedule(id,3)
    print(arrival)

if __name__ == '__main__':
    main()
