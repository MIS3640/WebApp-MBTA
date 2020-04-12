import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = 'usx5AjPsMDXCpwlQcnIp6mJ9HAnNxuNx'
MBTA_API_KEY = '4800dbf6194442a08871582e4d62887d'

# url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint(response_data)

# to print the postal code of Babson College
# print(response_data["results"][0]["locations"][0]['postalCode'])

# to extract the longitude and latitude of the JSON reponse for MAPQUEST
# print(response_data['results'][0]['locations'][0]['latLng'])

# to extract the station name of the JSON reponse for MBTA
print(response_data['data'][0]['attributes']['name'])

# to extract the wheelchair accesibility of the JSON reponse for MBTA
print(response_data['data'][0]['attributes']['wheelchair_boarding'])