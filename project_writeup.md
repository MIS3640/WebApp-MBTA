
### Project Description: 
The webapp created allows the user to input an address on a html page and then returns 
forwards the user to another page which contains information on the nearest MBTA stop 
and whether it is wheelchair accessible.
The project has been done in (Flask)[https://flask.palletsprojects.com/en/1.1.x/] which is a is a micro web framework written in Python.
The project utilises a number of [API](https://www.mulesoft.com/resources/api/what-is-an-api#:~:text=API%20is%20the%20acronym%20for,you're%20using%20an%20API.) requests.The first API used is the (MapRequest)[https://developer.mapquest.com/documentation/geocoding-api/address/get/] api which takes an address and get the associated latitude and longitude.The other API used here is the (MBTA-realtime)[https://api-v3.mbta.com/docs/swagger/index.html] which takes in the cordinates(latitude and longitude) of a place and finds the closest public transportation of that place.
 
### Functions: 
There are three major functions used in the project namely `get_address`, `lat_long` and `mbta`
 
#### get_address
This function takes in the address and returns a string containing no special characters
#### lat_long
This function takes in the address and returns the latitude and longitude of the place. It uses the `MapRequest` API mentioned earlier
### mbta
This function takes in the address and returns the name of the nearest MBTA station and a boolean value of whether the station is wheelchair accesible or not


### Project Reflection: 
Overall, this project went well given that we were able to create functional code. That being said, the code can always be improved by condensing it even further and making it more detailed like incorporating the distance to the nearest MBTA stop as well. The project was appropriately scoped and was more direct given that very few self-studying was conducted. The majority of the information needed was either in a previous class or in the links provided. We can now confidently use this material to create the foundation of our own websites.

Work was split in half, two group members worked on Part 1 and two worked on Part 2. Some issues while working together were that partner-programming is difficult most of the time, given that people read and think of code in a very different way. As a result of this, it’s hard to provide help when someone is writing code. Next time, we will aim to come up with a method in which all members can help each other while coding.
