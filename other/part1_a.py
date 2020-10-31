def latlng():

    import urllib.request
    import json
    from pprint import pprint

    MAPQUEST_API_KEY = "GIvTSav4ifuQ6OSObTVe7XzVoW5jB9Zq"

    url = f"http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    # pprint(response_data)

    """This is the structure of how required information
    is displayed in the dictionary:
    'latLng': {'lat': 39.91978, 'lng': -86.2158}

    'latLng' --> the key of the original dict

    {'lat': 39.91978, 'lng': -86.2158} --> respective values
    type:dict

    'lat' and 'lng' are two keys in this sub dict
    39.91978 and -86.2158 are two respective values"""

    # 1.access value in the original dict with key:latLng
    step1 = response_data["results"][0]["locations"][0]["latLng"]

    # 2a. access value for latitude in this sub-dict
    lat = step1.get("lat")

    # 3a. adjust positive/negative signs to north / south
    if lat > 0:
        latitude = f"{lat:.2f} north"
    else:
        latitude = f"{abs(lat):.2f} south"

    # 2b.access value for longtitude in this sub-dict
    lng = step1.get("lng")

    # 3b.adjust positive/negative signs to east/west
    if lng > 0:
        longtitude = f"{lng:.2f} east"
    else:
        longtitude = f"{abs(lng):.2f} west"

    outcome = f"the latitude of this place is {latitude} and the longtitude of this place is {longtitude}"

    return outcome


print(latlng())