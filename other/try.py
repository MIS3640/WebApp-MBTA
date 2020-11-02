# a = {"lat": 39.91978, "lng": -86.2158}
# for key in a:
#     (a.get(key))
#     print(a.get(key))
#     if a.get(key)>0:


# import urllib.request
# import json
# from pprint import pprint
# import urllib.parse

# MAPQUEST_API_KEY = "GIvTSav4ifuQ6OSObTVe7XzVoW5jB9Zq"
# location = "Babson College"
# # location_encoded = urllib.parse.quote(location)
# location_params = {"location": location}
# location_params = urllib.parse.urlencode(location_params)

# # url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location_encoded}"
# url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&{location_params}"
# f = urllib.request.urlopen(url)
# response_text = f.read().decode("utf-8")
# response_data = json.loads(response_text)
# pprint(response_data)


"""-----------------------------------------------------------------------"""
import urllib.request
import json
from pprint import pprint
import urllib.parse


def latlng(location):
    # location:str

    MAPQUEST_API_KEY = "GIvTSav4ifuQ6OSObTVe7XzVoW5jB9Zq"
    # 1. encoding the location name
    location_params = {"location": location}  # convert to a dict format to be encoded
    location_params = urllib.parse.urlencode(location_params)
    url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&{location_params}"

    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)

    step1 = response_data["results"][0]["locations"][0]["latLng"]
    latitude = step1.get("lat")
    longtitude = step1.get("lng")

    MBTA_API_KEY = "irvJ9dfg282UVAXk"
   
    lantitude_params = {"latitude": latitude}
    lantitude_params = urllib.parse.urlencode(lantitude_params)
    longtitude_params = {"longtitude": longtitude}
    longtitude_params = urllib.parse.urlencode(longtitude_params)
    
    url = f"https://api-v3.mbta.com/data/{lantitude_params}/attributes/latitude and /data/{longtitude_params}/attributes/longitude&?key={MBTA_API_KEY}"
    
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    # print(response_data)

    MBTA_API_KEY = "irvJ9dfg282UVAXk"

    # url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College"
    url = f"https://api-v3.mbta.com/data/{latitude}/attributes/latitude and /data/{longtitude}/attributes/longitude/?key={MBTA_API_KEY}"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    print(response_data)


print(latlng("Babson Colle")

#want to find a location,it has to have a station within a half mile