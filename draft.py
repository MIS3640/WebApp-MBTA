"""
Simple "Hello, World" application using Flask
"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

$ export FLASK_APP=app.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/



import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = 'bvd5kR5ANCpY295vIH5qgDEcpKZzeuKR'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
#pprint(response_data)
#pprint(response_data['results'][0]['locations'][0]['latLng'])

def long_lat(): 
    """
1. Write a function (maybe two) to extract the latitude 
and longitude from the JSON response.
    """
    MAPQUEST_API_KEY = 'bvd5kR5ANCpY295vIH5qgDEcpKZzeuKR'

    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data['results'][0]['locations'][0]['latLng'])
    lat = response_data['results'][0]['locations'][0]['latLng']['lat']
    longitude = response_data['results'][0]['locations'][0]['latLng']['lng']
    return lat, longitude

lat, longitude = long_lat()

# 2. Write a function that takes an address or place name 
# as input and returns a properly encoded URL to make 
# a MapQuest geocode request.

def mapquest_url(place_address): 
    url = 'http://www.mapquestapi.com/geocoding/v1/address?key=bvd5kR5ANCpY295vIH5qgDEcpKZzeuKR&location=' + place_address 
    return url 


# 3. Write a function that takes a latitude and longitude 
# and returns the name of the closest MBTA stop and 
# whether it is wheelchair accessible

def closest_mbta_stop(): 
    url1 = 'https://api-v3.mbta.com//stops?api_key=250359d96859421394c2f37d6c25e26d&filter[latitude]=42.352975&filter[longitude]=-71.055560&sort=distance'
    f = urllib.request.urlopen(url1)
    response_text2 = f.read().decode('utf-8')
    response_data2= json.loads(response_text2)
    stopName = (response_data2['data'][0]["attributes"]['name'])
    wheelchair_accessible = (response_data2['data'][0]["attributes"]['wheelchair_boarding'])
    print('The Closest Stop To You is: ',stopName)
    if wheelchair_accessible == 1: 
        print('It\'s wheelchair accessible')
    else: 
        print('it is not wheelchair accessible')

#print(closest_mbta_stop())



# 4. Combine your functions from the previous sections 
# to create a tool that takes a place name or address 
# as input, finds its latitude/longitude, and returns 
# the nearest MBTA stop and whether it is wheelchair 
# accessible.

def mbta_helper_tool(): 

    MAPQUEST_API_KEY = 'bvd5kR5ANCpY295vIH5qgDEcpKZzeuKR'
    location = input()

    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data['results'][0]['locations'][0]['latLng'])
    lat = response_data['results'][0]['locations'][0]['latLng']['lat']
    longitude = response_data['results'][0]['locations'][0]['latLng']['lng']

    url1 = 'https://api-v3.mbta.com//stops?api_key=250359d96859421394c2f37d6c25e26d&filter[latitude]=42.352975&filter[longitude]=-71.055560&sort=distance'
    f = urllib.request.urlopen(url1)
    response_text2 = f.read().decode('utf-8')
    response_data2= json.loads(response_text2)
    stopName = (response_data2['data'][0]["attributes"]['name'])
    wheelchair_accessible = (response_data2['data'][0]["attributes"]['wheelchair_boarding'])
    print('The Closest Stop To You is: ',stopName)
    if wheelchair_accessible == 1: 
        print('It\'s wheelchair accessible')
    else: 
        print('it is not wheelchair accessible')

mbta_helper_tool()

