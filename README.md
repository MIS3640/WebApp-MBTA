# WebApp-MBTA
 This is the base repo for MBTA project. Please read [instructions](instructions.md). 

For this project, I developed a website that gives the user the nearest MBTA location and whether it is wheelchair accessible. Although not a required function, I also included a functionality that allows the user to input the maximum distance they were willing to travel to get to the stop. This is beneficial because if the nearest stop is too far away it defeats the entire purpose of the transportation system. Once the user enters these fields, a quick validation is completed to ensure that the input is formatted correctly and that both fields are filled out. If not, the user will be redirected to an error page with a button that will take them back to the main page. They will also be directed to this page if the nearest transportation center is not within range. If they are successful in their request, they will be shown the results page which included wheelchair accessibility data and the name of the stop. They can then utilize a button on that page to navigate back to the main page. 

The backend is done well and works flawlessly. The front end could definitely be improved aesthetically. I had to do some self-studying to get a better understanding of HTML. I wish I had known the use case for the mbta_helper python program before I had finished writing it because I had to rewrite many of the functions to make it interface with the web application. In the future, I will definitely use CSS to improve the aesthetics of the page.

I was working alone, so dividing up the work was not an issue. I definitely should have budgeted more time to work on this project, and I underestimated the time it would take to complete this project. I also think that completing the MBTA helper script prior to beginning the website made development much quicker because I only had to troubleshoot one aspect of the project at a time.
