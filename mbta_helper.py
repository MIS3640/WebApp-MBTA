# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "TBDo2JHjPzxATo89WX0IaKybW0VRYtvf"
MBTA_API_KEY = "62eb3f8d91fe4bf3bc54d56c4d194cd8"


import urllib.request
import json


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    return response_data


# print(get_json(f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Copley%20Square"))


def get_lat_long(place_name, city):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    address = place_name.replace(" ", "%20")
    city = city.replace(" ", "%20")
    response_data = get_json(
        f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={address},{city},MA"
    )
    coordinates = response_data["results"][0]["locations"][0]["displayLatLng"]
    return coordinates


print(get_lat_long("Copley Square", "Boston"))


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    mbta = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    f1 = urllib.request.urlopen(mbta)
    response_text1 = f1.read().decode("utf-8")
    locale = json.loads(response_text1)
    stop_name = []
    stop_desc = []
    wheel_chair = []
    for element in locale["data"]:
        name = element["attributes"]["name"]
        desc = element["attributes"]["description"]
        wheelchair = element["attributes"]["wheelchair_boarding"]
        stop_desc.append(desc)
        stop_name.append(name)
        wheel_chair.append(wheelchair)
    for i in range(len(wheel_chair)):
        if wheel_chair[i] == 1:
            wheel_chair[i] = "Wheelchair Accessible"
        else:
            wheel_chair[i] = "Not Wheelchair Accessible"
    if len(stop_name) == 0:
        return "No Stops Nearby"
    elif stop_name[0] == "None":
        return stop_desc[0], wheel_chair[0]
    return stop_name[0], wheel_chair[0]


def test(location, city):
    lat_long = get_lat_long(location, city)
    latitude = lat_long.get("lat")
    longitude = lat_long.get("lng")
    mbta = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    f1 = urllib.request.urlopen(mbta)
    response_text1 = f1.read().decode("utf-8")
    locale = json.loads(response_text1)
    stop_name = []
    stop_desc = []
    wheel_chair = []
    for element in locale["data"]:
        name = element["attributes"]["name"]
        desc = element["attributes"]["description"]
        wheelchair = element["attributes"]["wheelchair_boarding"]
        stop_desc.append(desc)
        stop_name.append(name)
        wheel_chair.append(wheelchair)
    for i in range(len(wheel_chair)):
        if wheel_chair[i] == 1:
            wheel_chair[i] = "Wheelchair Accessible"
        else:
            wheel_chair[i] = "Not Wheelchair Accessible"
    if stop_name == "None":
        return "No Stops Nearby"
    return stop_name[0], wheel_chair[0]


def find_stop_near(place_name, city):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat_long = get_lat_long(place_name, city)
    latitude = lat_long.get("lat")
    longitude = lat_long.get("lng")
    return get_nearest_station(latitude, longitude)


def main():
    """
    You can test all the functions here
    """
    name = find_stop_near("410 Massachusetts Ave", "Boston")
    print(name)


if __name__ == "__main__":
    main()
