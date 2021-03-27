def get_mapquest_url(place_name):
    """
    Takes an address or place name as input
    Returns a properly encoded URL to make a MapQuest geocode request
    """
    import urllib.request
    import urllib.parse
    from config import MAPQUEST_API_KEY
    MAPQUEST_API_K = MAPQUEST_API_KEY
    params = urllib.parse.urlencode({'key': MAPQUEST_API_K, 'location': place_name})
    print(params)
    url = f'http://www.mapquestapi.com/geocoding/v1/address?%s' % params
    return url

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    import urllib.request
    import json
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
    MAPQUEST_URL = get_mapquest_url(place_name)
    response_data = get_json(MAPQUEST_URL) 
    lat = response_data['results'][0]['locations'][0]['displayLatLng']['lat']
    lng = response_data['results'][0]['locations'][0]['displayLatLng']['lng']
    return (lat, lng)
    

def get_nearest_station(latitude, longitude, route_type=None):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    # url = f'https://api-v3.mbta.com/stops/data/{index}/attributes/latitude and /data/{index}/attributes/longitude' % params
    # data = get_json(f"https://api-v3.mbta.com/stops?page%5Blimit%5D=1&sort=-distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}&filter%5Blocation_type%5D=1")
    import pprint
    from config import MBTA_API_KEY
    MBTA_API_K = MBTA_API_KEY
    MBTA_BASE_URL = "https://api-v3.mbta.com/stops?"
    url = f'{MBTA_BASE_URL}api_key={MBTA_API_KEY}&page%5Blimit%5D=1&sort=-distance&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&filter[route_type]={route_type}'
    data = get_json(url)
    print(data)
    return (data['data'][0]['attributes']['name'], data['data'][0]['attributes']['wheelchair_boarding'])


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat_long = get_lat_long(place_name)
    latitude = lat_long[0]
    longitude = lat_long[1]
    try:
        station = get_nearest_station(latitude, longitude)
        if station[1] == 1:
            nw_station = (f'The nearest station is {station[0]} and it is wheelchair accessible.')
        elif station[1] == 2:
            nw_station = (f'The nearest station is {station[0]} and it is not wheelchair accessible.')
        else:
            nw_station = (f'The nearest station is {station[0]} and there is no data on whether it is wheelchair accessible.')
        return nw_station
    except:
        error = ('The address was invalid or there are no stops nearby.')
        return error 
 

def main():
    from pprint import pprint
    
    # MAPQUEST_URL = get_mapquest_url("4 Jersey St, Boston, MA")
    # pprint(get_json(MAPQUEST_URL))
    # print(get_lat_long('21 Babson College Drive, Wellesley, MA 02482'))

    print(get_nearest_station(42.346786, -71.098649, 3))
    # print(find_stop_near("4 Jersey St, Boston, MA"))



if __name__ == '__main__':
    main()



