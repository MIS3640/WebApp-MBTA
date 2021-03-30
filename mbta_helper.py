import urllib.request
import json
import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "kJyQ1YOK8Ngxfk4u1J5TV8ITGQZuKG3m"
MBTA_API_KEY = "6af9e85ce354400281483fe6a6c1f27f"


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    return response_data


def get_lat_lng(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place_name = place_name.replace(" ", "%20")  # format URL correctly
    url = f"{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place_name}"

    response_data = get_json(url)  # get data from mapquest api
    lat = response_data["results"][0]["locations"][0]["latLng"]["lat"]
    lng = response_data["results"][0]["locations"][0]["latLng"]["lng"]
    return lat, lng


def get_nearest_station(lat, lng):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={lat}&filter[longitude]={lng}&sort=distance"
    response_data = get_json(url)

    station_name = response_data["data"][0]["attributes"][
        "name"
    ]  # retrieve station name from MBTA api
    wheelchair_boarding = response_data["data"][0]["attributes"][
        "wheelchair_boarding"
    ]  # retrieve wheelchair boarding info from MBTA api

    if wheelchair_boarding == 0:
        wheelchair_accessibility = "No Information"
    elif wheelchair_boarding == 1:
        wheelchair_accessibility = "Accessible"
    elif wheelchair_boarding == 2:
        wheelchair_accessibility = "Inaccessible"

    return station_name, wheelchair_accessibility


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, lng = get_lat_lng(place_name)
    station_name, wheelchair_accessibility = get_nearest_station(lat, lng)
    return station_name, wheelchair_accessibility


def main():
    """
    You can test all the functions here
    """
    # lat, lng = get_lat_lng('Boston University')
    # print(f'Latitude: {lat}, Longitude: {lng}')

    # station_name, wheelchair_accessibility = get_nearest_station(lat, lng)
    # print(f'{station_name}: {wheelchair_accessibility}')

    print(find_stop_near("Boston University"))


if __name__ == "__main__":
    main()
