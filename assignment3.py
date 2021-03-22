def get_url(place_name):
    """
    Takes an address or place name as input
    Returns a properly encoded URL to make a MapQuest geocode request
    """
    import urllib.request
    import urllib.parse
    from config import MAPQUEST_API_KEY
    MAPQUEST_API_KEY = MAPQUEST_API_KEY
    params = urllib.parse.urlencode({'key': MAPQUEST_API_KEY, 'location': place_name})
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
    MAPQUEST_URL = get_url(place_name)
    response_data = get_json(MAPQUEST_URL) 
    lat = response_data['results'][0]['locations'][0]['displayLatLng']['lat']
    lng = response_data['results'][0]['locations'][0]['displayLatLng']['lng']
    return (lat, lng)
    

def main():
    from pprint import pprint
    
    MAPQUEST_URL = get_url("Washington,DC")
    pprint(get_json(MAPQUEST_URL))
    print(get_lat_long('Washington,DC'))


if __name__ == '__main__':
    main()


