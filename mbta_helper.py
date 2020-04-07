# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "XbNTIQMhKz0tClvI7KVdJnGxdwp9Esvu"
MBTA_API_KEY = "ebcc79c2c7dc44d5b6f012325e8692d1"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    # locate = place_name.replace(' ','%20')
    link = f'{url}?key={MAPQUEST_API_KEY}'
    # url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={locate}'
    with urllib.request.urlopen(link) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        pprint(response_data)
        return(response_data)
        # print(response_data["results"][0]["locations"][0]['postalCode'])


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    # """
    # lag = source['results'][0]['locations'][0]['displayLatLng'][0]
    # print(lag)


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """


def main():
    """
    You can test all the functions here
    """
    print(get_json(MAPQUEST_BASE_URL) )
    # get_laglng(data)


if __name__ == '__main__':
    main()
