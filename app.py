"""
Simple "Hello, World" application using Flask
"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = 'bvd5kR5ANCpY295vIH5qgDEcpKZzeuKR'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
# pprint(response_data)

# 1. Write a function (maybe two) to extract the latitude 
# and longitude from the JSON response.

# 2. Write a function that takes an address or place name 
# as input and returns a properly encoded URL to make 
# a MapQuest geocode request.

# 3. Write a function that takes a latitude and longitude 
# and returns the name of the closest MBTA stop and 
# whether it is wheelchair accessible

# 4. Combine your functions from the previous sections 
# to create a tool that takes a place name or address 
# as input, finds its latitude/longitude, and returns 
# the nearest MBTA stop and whether it is wheelchair 
# accessible.

