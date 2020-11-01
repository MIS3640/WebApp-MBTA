# Project Reflection
### Shoaib R, Caroline B, and Susanna D.
### MIS 3640 Section 1
### 10/30/2020


## Project Overview *(1 paragraph )*

*Write a short abstract describing your project. Include all the extensions to the basic requirements.*

Our team worked on creating a program that would find the nearest mbta stop closest to the location the user would input. We launched this program, using flask, as a website. First, in order to create the program, we utilized the scaffolding functions Professor Li provided. The fuctions we build using that scaffolding call the corresponding longitude and latitude coordinates of the inputted location using the MapQuest API. These longitude and latitude coordinates were then used by another function to find the nearest station and return the name as well as wheelchair accessibilities, which were found through the MBTA API. In the final function, we layered the functions to seamlessly flow from a given location to the nearest MBTA stop. In order to create the website, our team utilized the html:5 templates to create 2 documents: one for the user to compute requirements and the other, for displaying results. 

## Project Reflection *(2 paragraphs )*

*After you finish the project, Please write a short document for reflection ~2 paragraphs*

From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? What self-studying did you do? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?

Also discuss your team process in your reflection. How did you plan to divide the work (e.g. split by class, always pair program together, etc.) and how did it actually happen? Were there any issues that arose while working together, and how did you address them? What would you do differently next time?

Our team originally planned to have our first meeting in order to go over the assignment 3 requirements and then divide the work. However, in our first meeting itself, we began pair programming and psuedo-coding that we roughly completed the first 3 out of 5 main functions for our program. We scheduled our next meeting and utilized the time in between to go over, rough code, comment, and become familiar with the entire goal of project and how we can implement it. In our next meeting, we paired programmed for more than 2 hours and completed the entire assignment's part 1 and 2. It definitely worked out differently than we had planned, but through clearly communicating during the calls and being able to help each other, it was probably even more successful than working individually on different parts as we were able to brainstorm creatively together, understand how all the functions are connected, and learn from each other. 

One thing our team did was underestimate the duration it would take us to build the functions. This would be something to consider in the future that we may approach differently. Had we known the amount of time it would take us to build a successful function, I believe we would have allocated our time in a more efficient way. For instance, rather than spending 2+ hours in two meetings time we could have had more shorter meetings. But we do not believe this affected the success of our assignment.

For the reflection aspect of the project, we felt we could divide the work up by each working on the paragraphs separately. Because we worked on the code all together, we were all on the same page and had the ability to work separately to contribute to the reflection. From a process point of view, we tested out "Wellesley Hills, Wellesley" as our test case to see if it would correctly give a "No Nearby Stations" response as intended. As well as testing "Copley Square, Boston" to check for a correct station response. Having this idea helped frequently test our code to see if we were on the right path or not.