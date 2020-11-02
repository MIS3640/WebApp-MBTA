import pprint
import urllib.request
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "W7jr5XPFwvxLfo6Tk4b3gCBXaz5NGPcu"
MBTA_API_KEY = "c4ad7c519f474f14b9aa1a13e7683218"


# A little bit of scaffolding if you want to use it


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    # print(response_data)
    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place_name = place_name.replace(" ", "%20")
    # url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College"
    url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}"
    response_data = get_json(url)
    # print(url)
    # pprint.pprint(response_data)
    # lat = response_data["results"][0]["locations"][0]['postalCode']

    # latitude = lat
    # latitude = response_data["results"][0]["locations"][0]['latLng']['lat]
    # longitude = lng
    # longitude = response_data["results"][0]["locations"][0]['latLng']['lng']
    # lat_long = response_data["results"][0]["locations"][0]['latLng']
    # return (lat_long.get('lat'), lat_long.get('lng'))
    lat = response_data["results"][0]["locations"][0]["latLng"]["lat"]
    lng = response_data["results"][0]["locations"][0]["latLng"]["lng"]
    return (lat, lng)


# print(get_lat_long())


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """

    # url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    url = f"https://api-v3.mbta.com/stops?sort=distance&api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}"
    response_data = get_json(url)

    try:
        station_name = response_data["data"][0]["attributes"]["name"]
        wheelchair_accessible = response_data["data"][0]["attributes"][
            "wheelchair_boarding"
        ]
        return station_name, wheelchair_accessible
    except IndexError as e:
        station_name = "No location found"
        wheelchair_accessible = 0
        return station_name, wheelchair_accessible

        # station_name = response_data["data"][0]["attributes"]["name"]
    # wheelchair_accessible = response_data["data"][0]["attributes"]["wheelchair_boarding"]

    # if wheelchair_accessible == 1:
    #     wheelchair_accessible = "Accessible"
    # elif wheelchair_accessible == 2:
    #     wheelchair_accessible = "Inaccessible"
    # else:
    #     wheelchair_accessible = "No Information"
    # return station_name, wheelchair_accessible


# print(get_nearest_station(42.3,71.27))


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, lon = get_lat_long(place_name)
    station_name, wheelchair_accessible = get_nearest_station(lat, lon)
    nearest_stop = f"Closest stop is {station_name}"
    if wheelchair_accessible:
        print("Wheelchair Accessible")
    else:
        print("Wheelchair Inaccessible")
    return (station_name, wheelchair_accessible)
    print(nearest_stop)


# print(find_stop_near("Babson College"))


def main():
    """
    You can test all the functions here
    """
    # place_name = input("Enter your location and state")

    # print(get_lat_long(place_name))

    # latitude = str(get_lat_long(place_name)[0])
    # longitude = str(get_lat_long(place_name)[1])
    # print(latitude)
    # print(longitude)

    # print(get_nearest_station(latitude,longitude))

    # print(find_stop_near("place_name"))
    # print(find_stop_near("Boston Common, MA"))
    # print(find_stop_near("Boston College, MA"))
    print(find_stop_near("Chinatown, MA"))


if __name__ == "__main__":
    main()
