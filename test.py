import requests #used requests package instead because it is bettter
import json
from pprint import pprint
MAPQUEST_API_KEY = 'wiGyI5fgWUoyGvlIFDarRqZwDSAD4Aoj'
location = ''
url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Boston'
response_text = requests.get(url)
print(response_text.encoding)