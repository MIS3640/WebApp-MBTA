import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = 'g0tGrEvT7Yr9QaysgxCNbJqMptavv8jf'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key=g0tGrEvT7Yr9QaysgxCNbJqMptavv8jf&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint(response_data)

def LatLong(data):
    print(response_data["results"][0]["locations"][0]['displayLatLng'])
    
LatLong(response_data)

import urllib.request
import urllib.parse
params = urllib.parse.urlencode({'Babson College': 1})
url = "http://www.mapquestapi.com/geocoding/v1/address?key=g0tGrEvT7Yr9QaysgxCNbJqMptavv8jf&location=?%s" % params
with urllib.request.urlopen(url) as f:
     print(f.read().decode('utf-8'))

import urllib.request
import json
from pprint import pprint
url = f'https://api-v3.mbta.com?api_key=bdf5f739ff0441e481b3a440299c9acc&filter[latitude]=42.349396&filter[longitude]=-71.078369&sort=distance'
f = urllib.request.urlopen(url)
response_text2 = f.read().decode('utf-8')
response_data2 = json.dumps(response_text2)
pprint(response_data2)


from flask import Flask

app = Flask(__name__)

@app.route('/hello')
@app.route('/<name>')
location = input ("PlaceName:" )
print full(location)