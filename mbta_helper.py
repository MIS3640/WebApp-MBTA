import urllib.request
import urllib.parse
import json
from pprint import pprint

def userlocation(location):
    # Write a function that takes an address or place name as input and returns a properly encoded URL to make a MapQuest geocode request.
    MAPQUEST_API_KEY = 'GIvTSav4ifuQ6OSObTVe7XzVoW5jB9Zq'
    location = {'location': location}
    location = urllib.parse.urlencode(location)
    map_base_url = "http://www.mapquestapi.com/geocoding/v1/address"
    map_url = f'{map_base_url}?key={MAPQUEST_API_KEY}&{location}'
    return map_url

def fetchmap(map_url):
    # Function that grabs MapQuest data 
    f = urllib.request.urlopen(map_url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data


def fetchlatlng(response_data):
    # Write a function (maybe two) to extract the latitude and longitude from the JSON response.
    coords = response_data["results"][0]["locations"][0]['latLng']
    latlng = {'lat':coords.get('lat'), 'lng':coords.get('lng')}
    return latlng


def fetchmbta(latlng, rad): 
    # Write a function that takes a latitude and longitude and returns the name of the closest MBTA stop and whether it is wheelchair accessible.
    MBTA_API_KEY = 'aa3640ae4bd645cda7374744202f217f'
    MBTA_BASE_URL = 'https://api-v3.mbta.com/stops'

    latitude = latlng.get('lat')
    longitude = latlng.get('lng')
    
    rad_convert = float(rad) * 0.2 # default to 0.01 degrees (approximately half a mile)

    mbta_url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&page[limit]=1&filter[radius]={rad_convert}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'

    f = urllib.request.urlopen(mbta_url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    
    # if len(response_data['data']) == 1:
    #     print(f"There are no MBTA stops within {rad} miles of your location.")

    stop_info = response_data["data"][0]["attributes"]
    stop_name = stop_info.get('name')
    stop_accessible = stop_info.get('wheelchair_boarding')

    if stop_accessible == 1:
        stop_accessible = "Yes"
    else: 
        stop_accessible = "No"
    print(f"Stop Name: {stop_name} \t Wheelchair Accessible: {stop_accessible}")
    return stop_name, stop_accessible
    


def main():
    location = input("Where would you like to search? ")
    rad = input("How many miles would you like to search? ")
    map_url = userlocation(location)
    response_data = fetchmap(map_url)
    latlng = fetchlatlng(response_data)
    # fetchmbta(latlng, rad)
    fetchmbta(latlng, rad)

if __name__ == '__main__':
    main()

#####################################################################
# def fetchlat(latlng):
#     # Write a function (maybe two) to extract the latitude and longitude from the JSON response.
#     lat = str(latlng.get('lat'))
#     return lat
# def fetchlng(latlng):
#     # Write a function (maybe two) to extract the latitude and longitude from the JSON response.
#     lng = str(latlng.get('lng'))
#     return lng

# latitude = {'latitude':latlng.get('lat')}
# latitude = urllib.parse.urlencode(latitude)

# longitude ={'longitude':latlng.get('lng')}
# longitude = urllib.parse.urlencode(longitude)

# location = location.encode('ascii') # Does not work
