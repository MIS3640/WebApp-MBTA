import json
import enum
import urllib
import urllib.request

MAPQUEST_API_KEY = "t9ax7GBATELvZ9T5ARi4IPqgxsIVQjEf"

MBTA_API_KEY = "8dce7e8198c94c478e813c41559c1a29"


class WheelchairBoarding(enum.IntEnum):
    no_information = 0,
    accessible = 1,
    inaccessible = 2


class StopNotFoundError(Exception):
    pass


def main():
    location = input("Please enter an address or a place name: ")
    try:
        stop = find_nearest_stop(location)
        print("Name: " + stop["name"])
        print("Description: " + stop["description"])
        print("Coordinates: " + str(stop["latitude"]) + "," + str(stop["longitude"]))
        if stop["wheelchair_boarding"] == WheelchairBoarding.accessible:
            print(stop["name"] + " is accessible.")
        elif stop["wheelchair_boarding"] == WheelchairBoarding.inaccessible:
            print(stop["name"] + " is inaccessible.")
        else:
            print("There is no information about accessibility")
        print(stop["wheelchair_boarding"])
        print("Google maps page: " + google_maps(stop["latitude"], stop["longitude"]))
        print("Street view page: " + street_view(stop["latitude"], stop["longitude"]))

    except StopNotFoundError:
        print("Stop not found.")


def address(location):
    endpoint = "http://www.mapquestapi.com/geocoding/v1/address"
    data = dict()
    data["key"] = MAPQUEST_API_KEY
    data["location"] = location

    query_string = urllib.parse.urlencode(data)
    url = endpoint + "?" + query_string
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response = json.loads(response_text)
    lat_lng = get_lat_lng(response)
    return lat_lng


def get_lat_lng(response):
    return response["results"][0]["locations"][0]["latLng"]


def closest_stop(coordinates):
    endpoint = "https://api-v3.mbta.com/stops"
    data = dict()
    data["api_key"] = MBTA_API_KEY
    params = {
        "filter[latitude]": coordinates["lat"],
        "filter[longitude]": coordinates["lng"]
    }

    query_string = urllib.parse.urlencode(params)
    url = endpoint + "?" + query_string
    req = urllib.request.Request(url)
    req.add_header("accept", "application/vnd.api+json")
    f = urllib.request.urlopen(req)
    response_text = f.read().decode('utf-8')
    response = json.loads(response_text)
    if len(response["data"]) == 0:
        raise StopNotFoundError
    return response["data"][0]


def find_nearest_stop(location):
    coordinates = address(location)
    stop = closest_stop(coordinates)
    return {
        "id": stop["id"],
        "name": stop["attributes"]["name"],
        "description": stop["attributes"]["description"],
        "latitude": stop["attributes"]["latitude"],
        "longitude": stop["attributes"]["longitude"],
        "wheelchair_boarding": WheelchairBoarding(stop["attributes"]["wheelchair_boarding"]),
    }


def google_maps(latitude, longitude):
    return "https://www.google.com/maps/search/?api=1&query={0},{1}".format(latitude, longitude)


def street_view(latitude, longitude):
    return "https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={0},{1}".format(latitude, longitude)


if __name__ == "__main__":
    main()
