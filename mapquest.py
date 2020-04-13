import requests #used requests package instead because it is bettter
import json
from pprint import pprint
import math

def initialize():
    MAPQUEST_API_KEY = 'wiGyI5fgWUoyGvlIFDarRqZwDSAD4Aoj'
    location = get_userlocation()
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location}'
    response_text = requests.get(url)
    response_data = response_text.json()
    return(response_data)

def get_latlng():
    json_data = initialize()
    lat = json_data["results"][0]["locations"][0]['displayLatLng']['lat']
    lng = json_data["results"][0]["locations"][0]['displayLatLng']['lng']
    return [lat, lng]

def get_userlocation():
    location = input('Please enter your desired location: ')
    return location

def get_closeststop():
    try:
        latlng = get_latlng()
        #api_key = '9d93eec9ab1449138c2bb1afcc161327' #i dont think you even need this???
        longitude = latlng[1]
        latitude = latlng[0]
        url = f'https://api-v3.mbta.com/stops/?filter[latitude]={latitude}&filter[longitude]={longitude}'
        response_text = requests.get(url)
        # print(response_text.status_code)
        response_data = response_text.json()
        #pprint(response_data)
        stoplatlng = []
        for i in range(len(response_data['data'])):
            if response_data['data'][i]['attributes']['vehicle_type'] == 1:
                stoplatlng.append([response_data['data'][i]['attributes']['latitude'],response_data['data'][i]['attributes']['longitude']])
        distance = []
        for i in range(len(stoplatlng)):
            dist = math.sqrt(((latitude - stoplatlng[i][0]) ** 2) + ((longitude - stoplatlng[i][1]) ** 2))
            distance.append(dist)
        shortest_distance = distance[0]
        for dist in distance:
            if dist < shortest_distance:
                shortest_distance = dist
        index = 0
        for i in range(len(distance)):
            if shortest_distance == distance[i]:
                break
            else:
                index +=1
        shortest_distancelatlng = stoplatlng[index]
        latitude = shortest_distancelatlng[0]
        longitude = shortest_distancelatlng[1]
        for i in range(len(response_data['data'])):
            if response_data['data'][i]['attributes']['latitude'] == latitude and response_data['data'][i]['attributes']['longitude'] == longitude:
                name = response_data['data'][i]['attributes']['name']
                print(name)
                if response_data['data'][i]['attributes']['wheelchair_boarding'] == 1:
                    print('This stop has wheelchair boarding')
                else:
                    print('No wheelchair boarding here')
                break 
    except:
        print('There are no T stops in the list')


    # for i in range(len(response_data['data'])):
    #     if response_data['data'][i]['attributes']['vehicle_type'] == 1:
    #         closest_stop = response_data['data'][i]['attributes']['name']
    #         print(closest_stop)
            


    

get_closeststop()

