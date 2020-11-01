import urllib.request
import urllib.parse
import json
from pprint import pprint


def userlocation(location):
    """Takes an address or place name as input and returns a properly encoded URL.

    Keyword arguments:
    location -- User input from MBTA form.
    """
    MAPQUEST_API_KEY = "GIvTSav4ifuQ6OSObTVe7XzVoW5jB9Zq"
    location = {"location": location}
    location = urllib.parse.urlencode(location)
    map_base_url = "http://www.mapquestapi.com/geocoding/v1/address"
    map_url = f"{map_base_url}?key={MAPQUEST_API_KEY}&{location}"
    return map_url


def fetchmap(map_url):
    """Takes the URL and handles data from MapQuest. Returns a dictionary.

    Keyword arguments:
    map_url -- URL used to get the MapQuest data.
    """
    f = urllib.request.urlopen(map_url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    return response_data


def fetchlatlng(response_data):
    """Extracts the latitude and longitude from the JSON response. Returns a dictionary.

    Keyword arguments:
    response_data -- Data from MapQuest.
    """
    coords = response_data["results"][0]["locations"][0]["latLng"]
    latlng = {"lat": coords.get("lat"), "lng": coords.get("lng")}
    return latlng


def fetchmbta(latlng, rad):
    """Uses latitude, longitude, and radius to return the closest MBTA stop and whether it is wheelchair accessible.

    Keyword arguments:
    latlng -- Dictionary that contains latitude and longitude values.
    rad -- User input for radius of search.
    """
    MBTA_API_KEY = "aa3640ae4bd645cda7374744202f217f"
    MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

    latitude = latlng.get("lat")
    longitude = latlng.get("lng")

    rad_convert = (
        float(rad) * 0.2
    )  # default to 0.01 degrees (approximately half a mile)

    mbta_url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&page[limit]=1&filter[radius]={rad_convert}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"

    f = urllib.request.urlopen(mbta_url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)

    # if len(response_data['data']) == 1:
    #     print(f"There are no MBTA stops within {rad} miles of your location.")

    stop_info = response_data["data"][0]["attributes"]
    stop_name = stop_info.get("name")
    stop_accessible = stop_info.get("wheelchair_boarding")

    if stop_accessible == 1:
        stop_accessible = "Yes"
    else:
        stop_accessible = "No"
    return stop_name, stop_accessible


def main():
    """Define keyword arguments."""
    location = input("Where would you like to search? ")
    rad = input("How many miles would you like to search? ")
    map_url = userlocation(location)
    response_data = fetchmap(map_url)
    latlng = fetchlatlng(response_data)
    fetchmbta(latlng, rad)


if __name__ == "__main__":
    main()
