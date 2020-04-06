import urllib.request
import urllib.parse
import json
from pprint import pprint


def takeUserInput(key):
    secondParam = input("Enter the location:")
    params = {'key': key, 'location': secondParam}
    a = urllib.parse.urlencode(params)
    return (f'http://www.mapquestapi.com/geocoding/v1/address?' + str(a))


def getCoordinates():

    MAPQUEST_API_KEY = 'JNVOQp6Yig9sib6RVBnpbBpbirMOzyG1'
    url = takeUserInput(MAPQUEST_API_KEY)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)

    locLen = 0  # sections counts the number of locations
    for x in (response_data["results"][0]["locations"]):
        locLen = locLen + 1
    print ("LocLen is " + str(locLen))
    count = 0
    if locLen ==0: print("No location found.")
    elif locLen ==1:  #condition when one location comes up thats not MA
        if response_data["results"][0]["locations"][0]["adminArea3"] != 'MA':
            print("ERROR: MA LOCATION NOT FOUND")
            exit() # exits code because you can't do anything
    else: #when there is more than one location
        while(count != locLen-1):
            if response_data["results"][0]["locations"][count]["adminArea3"] == 'MA':
                break
            else:
                count = count + 1

        if response_data["results"][0]["locations"][count]["adminArea3"] != 'MA': # exists if last loc is not MA
            print("ERROR: MA LOCATION NOT FOUND.")
            exit()
    return response_data["results"][0]["locations"][count]["displayLatLng"]

def getNearestLocation(latLngArray):
    mbta_api_key = 'd657ba4068af473bb42cff137b163785'
    url = f'https://api-v3.mbta.com/stops?api_key=9d7fbfd56c164a2bbedb3691a1a79949&filter%5Blatitude%5D='\
          +str(latLngArray['lat'])+'&filter%5Blongitude%5D='\
          +str(latLngArray['lng'])
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)
    print(response_data["data"][0]["attributes"]["name"])
    if response_data["data"][0]["attributes"]["wheelchair_boarding"] == 0:
        print("No information on wheelchair boarding")
    elif response_data["data"][0]["attributes"]["wheelchair_boarding"] == 1:
        print("	Accessible (if trip is wheelchair accessible)")
    else:
        print("Inacessible")

latLngArray = (getCoordinates())
print("-------------------------------------------------------------------------------------------------------------")
getNearestLocation(latLngArray)