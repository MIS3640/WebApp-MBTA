import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = 'usx5AjPsMDXCpwlQcnIp6mJ9HAnNxuNx'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint(response_data)

# to print the postal code of Babson College
# print(response_data["results"][0]["locations"][0]['postalCode'])

# to extract the longitude and latitude of the JSON reponse
print(response_data['results'][0]['locations'][0]['latLng'])