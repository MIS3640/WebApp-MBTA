import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = 'g0tGrEvT7Yr9QaysgxCNbJqMptavv8jf'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key=g0tGrEvT7Yr9QaysgxCNbJqMptavv8jf&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint(response_data)

def lat_long(place_name):
    for location in response_data:
        print (response_data.latlng)