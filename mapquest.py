import requests #used requests package instead because it is bettter
import json
from pprint import pprint

def initialize():
    MAPQUEST_API_KEY = 'wiGyI5fgWUoyGvlIFDarRqZwDSAD4Aoj'
    location = get_userlocation()
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location}'
    response_text = requests.get(url)
    response_data = response_text.json()
    return(response_data)

def get_latlng():
    json_data = initialize()
    lat = json_data["results"][0]["locations"][0]['displayLatLng']['lat']
    lng = json_data["results"][0]["locations"][0]['displayLatLng']['lng']
    return [lat, lng]

def get_userlocation():
    location = input('Please enter your desired location: ')
    return location

def get_closeststop():
    latlng = get_latlng()
    index = '9d93eec9ab1449138c2bb1afcc161327'
    longitude = latlng[1]
    latitude = latlng[0]
    url = f'https://api-v3.mbta.com/stops/'
    #filter[latitude]={latitude}&filter[longitude]={longitude}'
    response_text = requests.get(url)
    print(response_text.status_code)
    response_data = response_text.json()
    pprint(response_data)


    

get_closeststop()

