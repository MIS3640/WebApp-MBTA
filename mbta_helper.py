# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "GIvTSav4ifuQ6OSObTVe7XzVoW5jB9Zq"
MBTA_API_KEY = "018aca1b39d94e2dbf05251d238b2949"


# A little bit of scaffolding if you want to use it


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    import urllib.request
    import json
    from pprint import pprint

    MAPQUEST_API_KEY = "GIvTSav4ifuQ6OSObTVe7XzVoW5jB9Zq"

    url = f"{url}?key={MAPQUEST_API_KEY}&location=Babson%20College"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    return pprint(response_data)


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    # location:str

    import urllib.request
    import json
    from pprint import pprint
    import urllib.parse

    MAPQUEST_API_KEY = "GIvTSav4ifuQ6OSObTVe7XzVoW5jB9Zq"
    # 1. encoding the location name
    location_params = {"location": place_name}  # convert to a dict format to be encoded
    location_params = urllib.parse.urlencode(location_params)
    url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&{location_params}"

    # 2.extract data
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)

    """This is the structure of how required information in part1_a.py(Babson College)
    is displayed in the dictionary:
    'latLng': {'lat': 39.91978, 'lng': -86.2158}

    'latLng' --> the key of the original dict

    {'lat': 39.91978, 'lng': -86.2158} --> respective values
    type:dict

    'lat' and 'lng' are two keys in this sub dict
    39.91978 and -86.2158 are two respective values"""

    # 1.access value in the original dict with key:latLng
    step1 = response_data["results"][0]["locations"][0]["latLng"]

    # 2. access value for latitude and longtitude in this sub-dict
    lat = step1.get("lat")
    lng = step1.get("lng")

    result = (lat, lng)

    return f"The latitude and lontitdue of {place_name} is {result}"


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    import urllib.request
    import json
    from pprint import pprint

    # # This is the test location lantitude and longtitude of Chinatown Boston
    # latitude = 42.3482482
    # longitude = -71.0676009

    MBTA_API_KEY = "018aca1b39d94e2dbf05251d238b2949"
    MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

    url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"

    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    # pprint(response_data)

    attributes_assortment = response_data["data"]

    # pprint(attributes_assortment)

    for f in attributes_assortment:
        # pprint(f)
        try:
            stop_type = f["relationships"]["zone"]["data"]["id"]
        except TypeError as e:
            pass  #  print(e)
        finally:

            if stop_type == "RapidTransit":

                result_name = f["attributes"]["name"]
                # print(result_name)
                wheelchair_info = f["attributes"]["wheelchair_boarding"]
                if wheelchair_info == 0:
                    wheelchair_accessibility = "No Information"
                elif wheelchair_info == 1:
                    wheelchair_accessibility = "Accessible"
                elif wheelchair_info == 2:
                    wheelchair_accessibility = "Inaccessible"
                break
    return f"According to the location entered, the closest MBTA station is {result_name}. The wheelchair service is {wheelchair_accessibility}"


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """

    """Step 1: get latitude and longtitude of the location"""
    # location:str

    import urllib.request
    import json
    from pprint import pprint
    import urllib.parse

    MAPQUEST_API_KEY = "GIvTSav4ifuQ6OSObTVe7XzVoW5jB9Zq"
    # 1. encoding the location name
    location_params = {"location": place_name}  # convert to a dict format to be encoded
    location_params = urllib.parse.urlencode(location_params)
    url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&{location_params}"

    # 2.extract data
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)

    # 3.obtain latitiude and longtitude
    step1 = response_data["results"][0]["locations"][0]["latLng"]
    lat = step1.get("lat")
    lng = step1.get("lng")

    """Step 2: Find the closest stop and check wheelchair accessibility"""
    MBTA_API_KEY = "018aca1b39d94e2dbf05251d238b2949"
    MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

    url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={lat}&filter[longitude]={lng}&sort=distance"

    f = urllib.request.urlopen(url)
    response_text2 = f.read().decode("utf-8")
    response_data2 = json.loads(response_text2)
    # pprint(response_data)

    attributes_assortment = response_data2["data"]

    # pprint(attributes_assortment)

    for f in attributes_assortment:
        # pprint(f)
        try:
            stop_type = f["relationships"]["zone"]["data"]["id"]
        except TypeError as e:
            pass  #  print(e)
        finally:

            if stop_type == "RapidTransit":

                result_name = f["attributes"]["name"]
                # print(result_name)
                wheelchair_info = f["attributes"]["wheelchair_boarding"]
                if wheelchair_info == 0:
                    wheelchair_accessibility = "No Information"
                elif wheelchair_info == 1:
                    wheelchair_accessibility = "Accessible"
                elif wheelchair_info == 2:
                    wheelchair_accessibility = "Inaccessible"
                break
    return f"According to the location entered, the closest MBTA station is {result_name}. The wheelchair service is {wheelchair_accessibility}"


def main():
    """
    You can test all the functions here
    """
    # print(get_json(MAPQUEST_BASE_URL))
    print(get_lat_long("Chinatown Boston"))
    # print(get_nearest_station(42.3482482, -71.0676009))
    # This is the location of Tufts Medical Center Station
    # print(find_stop_near("Chinatown Boston"))


if __name__ == "__main__":
    main()