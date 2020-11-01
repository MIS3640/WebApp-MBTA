**Project Overview**

This project is basically a python Flask web application that can help you find the nearest MBTA station from a specific location. The applicaiton structure can be splited into two parts as front-end and bakc-end. 

The front-end is composed of two pages. In the index/search page, user can input a place name and submit the query. Then it will redirect to the result page showing the nearest MBTA station's name and wheelchair accessibility. If the service cannot find a station 1 mile near your place, the page will tell you no station there.

The back-end basically wrapped two web service APIs Mapquest api and MBTA api V3. Our own service accepts only one parameter, which is place name. Then queries Maprequest to convert it to latitude, longitude pairs. At last, using lat & lng to query MBTA api and return the related MBTA information.

**Project Reflection**

For the basic requirements, the process went well. While implementing the mbta_helper.py, we firstly got api keys from both Maprequest and MBTA api V3. Then we completed several methods and finally wrapped them up to a method find_stop_near for web back-end service calling. As for front-end, we quickly go thorugh the Flask tutorial and successfully implemented the web pages.

Besides the basic requirements, we could improve the front-end user interface or provide more options to users. For instance, we could utilise more MBTA apis such as Facility, Line, Route, Schedule, Trip and so on. By using more apis, we can enhance our web pages' functionality. For unit testing, we just simply test mbta_helper.py by running methods and checking print results. To do better in testing, we could use python libraries like pytest.

Overall, it was good that we quickly learned two geo apis and Flask framework. And we finally make the deliverables. We can learn more about Flask to develop a fancier web application in the future.