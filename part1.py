import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = "BpynYpgD1n4YX5fTyC6d41TAqEMG7O6K"


def get_address(address):
    addyy = f"{address}"
    return addyy.replace(" ", "+")



def lat_long(address):
    geo_location = get_address(address)
    url = f"https://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={geo_location}"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    x = response_data["results"][0]["locations"][0]["displayLatLng"]
    latitude = x["lat"]
    longitude = x["lng"]
    return latitude, longitude
    

mbta_key = "f0b7b92a7e14424dbcb76de3faf2bb34"


def mbta(address):
    wheelchair_access = False
    x = lat_long(address)
    latitude, longitude = x 
    url = f"https://api-v3.mbta.com/stops?page%5Blimit%5D=1&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    name = response_data["data"][0]["attributes"]["name"]
    wheelchair = response_data["data"][0]["attributes"]["wheelchair_boarding"]
    if wheelchair == 1:
        wheelchair_access = True
    return name, wheelchair_access


# pprint(mbta("150 untingggton Ave boston ma"))