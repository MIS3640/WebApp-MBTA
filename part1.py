import urllib.request
import json
from pprint import pprint
import urllib.parse

#example locations
'Boston,MA'
'Wellesley,MA'
'Chelsea,MA'
'Brookline,MA'

print('Input your current location to find the nearest MBTA stop')
name = input()
def lat_long(location): 
    """
    Function that gets the information of a location based on its name. 
    """
    global data_latlong
    print('Your location is',location)
    #Imports data from the mapquestapi
    MAPQUEST_API_KEY = 'XxtdAMBvWmSKhAKu0wu0kMXQT8gbOp6b'
    # url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    url = (f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={name}')
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    data_latlong = json.loads(response_text)
    # pprint(response_data)

# lat_long(name)

def stop(datas):
    """
    Function that prints the closest MBTA stop based on the latitude and longitude. 
    """
    MBTA_API_KEY = '78c78742ffb14c3cb6b22071c0986b51'
    
    #Gets the latitude and longitude
    lat = datas["results"][0]["locations"][0]['displayLatLng']['lat']
    long = datas["results"][0]["locations"][0]['displayLatLng']['lng']
    # print('lat',lat)
    # print('long',long)

    #imports data from the mbta api
    url1 = (f"https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={long}")
    f = urllib.request.urlopen(url1)
    response_text1 = f.read().decode('utf-8')
    response_data1 = json.loads(response_text1)
    # pprint(response_data1)

    #Gets the name, at street and on street of the stop
    stop_name = response_data1["data"][0]["attributes"]['name']
    stop_atstreet = response_data1["data"][0]["attributes"]['at_street']
    stop_onstreet = response_data1["data"][0]["attributes"]['on_street'] 
    print(f'The name of the stop is {stop_name}. It is at the street {stop_atstreet} and on the street {stop_onstreet}.')

    #Gets whether the stop is wheelchair accesible
    wheel = response_data1["data"][0]["attributes"]['wheelchair_boarding']
    # print("Has wheelchair access:", response_data1["data"][0]["attributes"]['wheelchair_boarding'])
    
    #Based on the whether the stop is accesible, the result is printed in a more user friendly format
    if wheel == 0: 
        print('There is no information for whether the stop is wheelchair accessible')
    elif wheel == 1:
        print('The stop is accessible to wheelchairs')
    elif wheel == 2:
        print('The stop is inaccessible to wheelchairs')

    # print('lat1', lat)
    # print('long1', long)   


# stop(data_latlong)
# print('lat2', lat)
# print('long2', long)
def main():
    lat_long(name)
    stop(data_latlong)


if __name__ == "__main__":
    main()

#example locations
'Boston,MA'
'Wellesley,MA'
'Chelsea,MA'
'Brookline,MA'
