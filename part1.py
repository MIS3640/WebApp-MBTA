import urllib.request
import json
from pprint import pprint
import urllib.parse

lat = 0
long = 0
data_latlong = 0
# import mbta_helper
# print(mbta_helper.find_stop_near("Boston Common"))
print('Input location')
name = input()
def lat_long(location): 
    global data_latlong
    print('The location is ',location)
    MAPQUEST_API_KEY = 'XxtdAMBvWmSKhAKu0wu0kMXQT8gbOp6b'
    # url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    url = (f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={name}')
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    data_latlong = json.loads(response_text)
    # pprint(response_data)

lat_long(name)


def stop(datas):
    MBTA_API_KEY = '78c78742ffb14c3cb6b22071c0986b51'
    # global lat
    # global long
    lat = datas["results"][0]["locations"][0]['displayLatLng']['lat']
    long = datas["results"][0]["locations"][0]['displayLatLng']['lng']
    print('lat',lat)
    print('long',long)
    # lat = 42.358894
    # long = -71.056742
    # print("The latitude is:", datas["results"][0]["locations"][0]['displayLatLng']['lat'])
    # print("The longitude is:", datas["results"][0]["locations"][0]['displayLatLng']['lng'])
    url1 = (f"https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={long}")
    f = urllib.request.urlopen(url1)
    response_text1 = f.read().decode('utf-8')
    response_data1 = json.loads(response_text1)
    # pprint(response_data1)
    print("Name:", response_data1["data"][0]["attributes"]['name'])
    print("At street:", response_data1["data"][0]["attributes"]['at_street'])
    print("On street:", response_data1["data"][0]["attributes"]['on_street'])
    wheel = response_data1["data"][0]["attributes"]['wheelchair_boarding']
    # print("Has wheelchair access:", response_data1["data"][0]["attributes"]['wheelchair_boarding'])
    if wheel == 0: 
        print('There is no information for whether the stop is wheelchair accessible')
    elif wheel == 1:
        print('The stop is accessible to wheelchair')
    elif wheel == 2:
        print('The stop is inaccessible to wheelchair')

    # print('lat1', lat)
    # print('long1', long)   


stop(data_latlong)
# print('lat2', lat)
# print('long2', long)
'Boston,MA'
'Wellesley,MA'
# Chelsea,MA
'Washington,DC'
'Chelsea,MA'

# MBTA_API_KEY = '78c78742ffb14c3cb6b22071c0986b51'
# # lat = 42.358894
# # long = -71.056742
# # curl -X GET "https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D=42.358894&filter%5Blongitude%5D=--71.056742" 
# url1 = (f"https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={long}")
# f = urllib.request.urlopen(url1)
# response_text1 = f.read().decode('utf-8')
# response_data1 = json.loads(response_text1)
# # pprint(response_data1)
# print("At street:", response_data1["data"][0]["attributes"]['at_street'])
# print("On street:", response_data1["data"][0]["attributes"]['on_street'])

