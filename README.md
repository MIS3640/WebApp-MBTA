# WebApp-MBTA - Mateos
[View project reflection here](project_writeup.md)
Simple WebApp that takes in a location input, using MapQuest's Place Search API, converts the location to a latitude and longitude, and then returns the nearest MBTA stop to that location and displays it on a map. 

# Instructions
1. Fill out sensitive.txt with the correct keys (MAPQUEST_API_KEY and PLACE_SEARCH_KEY can be the same)
2. Activate virtual environment where the web app is installed using venv\Scripts\activate
3. Set the flask app to app.py using set FLASK_APP = app.py
4. Start the app using flask run
5. Navigate to http://127.0.0.1:5000/
6. Type in a location and select one of the suggestions from the typeahead
7. Click search

