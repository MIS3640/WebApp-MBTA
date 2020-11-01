import urllib.request
import json
from pprint import pprint
import urllib.parse
from flask import Flask

MAPQUEST_API_KEY = 'g0tGrEvT7Yr9QaysgxCNbJqMptavv8jf'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key=g0tGrEvT7Yr9QaysgxCNbJqMptavv8jf&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint(response_data)

def LatLong(data):
    print(response_data["results"][0]["locations"][0]['displayLatLng'])
    
LatLong(response_data)


params = urllib.parse.urlencode({'Babson College': 1})
url = "http://www.mapquestapi.com/geocoding/v1/address?key=g0tGrEvT7Yr9QaysgxCNbJqMptavv8jf&location=?%s" % params
with urllib.request.urlopen(url) as f:
     print(f.read().decode('utf-8'))



app = Flask(__name__)

@app.route('/hello')
@app.route('/<name>')
loc = input ("PlaceName:" )
print full(loc)

#aa