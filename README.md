         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!

   <!--<nav>-->
   <!--     <ul>-->
   <!--         <li><a href="{{url_for('index')}}">home</a></li>-->
   <!--         <li><a href="{{url_for('recipes')}}">recipes</a></li>-->
   <!--           <li><a href="{{url_for('directions')}}">directions</a></li>-->
   <!--     </ul>-->
   <!-- </nav>-->
    
   <!--  <div class="container">-->

   <!--     {% block content %} -->
   <!--        <h1>home page</h1>-->
        
   <!--     {% endblock %}-->
   <!-- </div>-->

<!--https://startbootstrap.com/previews/business-casual/ resource-->
<!--https://codeburst.io/alter-table-examples-with-mysql-beginner-series-7e8ca2a58ce2-->
<!--mysqldatabase refference-->\

<!--modify and cleaned up code-->
<!--added run.py file apps-->
<!--edited apps-->
<!--downloaded mysql-->
<!--create query-->

<!--https://www.goodhousekeeping.com/food-recipes/a39354/mexican-breakfast-chilaquiles-recipe/-->
<!--https://stackoverflow.com/questions/52256510/bootstrap-image-uploader --> 
<!--^source for button-->
<!--https://www.lucidchart.com/documents/edit/6ac52063-c50e-4f00-84e6-97cbd4ef2848/YGcM5DNywbTK?shared=true&useCachedRole=false-->
<!--link to databases-->
<!--https://www.allrecipes.com/video/1024/asian-orange-chicken/ *source for asian dishes-->
<!--https://github.com/daveozoalor/bootstrap4-udemy-clone/blob/master/index.html * source for the toolbar at bottom of page-->
1.<!--Want to add feature--- most recent recpies------ dynamic deisplay and our most poplular recipes dynamic display -->
 2.<!-- Feature a recent recipe Section (wanted to add section of readme)  <!--Image of the most recent dynamically displayed picture seen here-->
 ---Our most pupular recipes advertisment panel for ideas-- cards X3 --><!--    <h2>Our Most Recent Recipes</h2>-->
#Cookbook | Flask & PostgreSQL Data Centric Development Project
#UX Design
. This folder contains documents that illustrate the user interface design by way of wireframe mockups of the main web pages of the application.

#Database Design
Details of the Database design is available in the 'Database Schema' folder. The ERD (Entity Relationship Diagram) document outlines how I approached the design of the Database.

#Features
Existing Features
This is a web application which that allows users to store and easily access cooking recipes. It is a full stack web application (frontend and backend) that provides CRUD (Create, Read, Update, Delete) functionality to a database hosted in the cloud on Heroku platform as a service. Users can :

#Recipe Search: search by recipe name, search by ingredient and filter recipes by category, course, cuisine and author on the index page.
Add Recipe: Add a new recipe and then Add ingredients and methods to the recipe on the recipe detail page.
Manage Categories: Add new and Edit existing static data like categories, courses, cuisines, authors, measurements etc.
My Recipes: view a list of recipes submitted by the current logged in user.
Saved Recipes: view and manage a list of recipes saved by the current logged in user.
Dashboard: displays interactive dashboard of charts; Categories bar chart, courses pie chart, cuisines row chart and author bar chart.
Recipe Detail: Save, Edit and Delete recipes, Edit and Delete ingredients, Edit and Delete methods.
Features Left to Implement
Allergens and Dietary
Demo
A demo of this web application is available here.

Getting started /
Clone the repo and cd into the project directory.
Ensure you have Python 3 and Postgres installed and create a virtual environment and activate it.
Install dependencies: pip install -r requirements.txt.
Technologies Used
HTML, CSS, JavaScript (Front End Framework Materialize) Python, Full Stack Micro Framework Flask, PostgreSQL an object-relational database management system :

Testing
Automated tests were carried out and all 47 tests passed satisfactorily (see screenshot in Testing folder). They are located in the file tests.py and can be ran using the command: python3 tests.py

Manual testing was undertaken for this application and satisfactorily passed. A sample of the tests conducted are as follows:

Testing navigation buttons and hyperlinks throughout the page
Testing the CRUD functionality
Testing the responsiveness of the application on different browsers and then using different devices.
Deployment
Make sure requirements.txt and Procfile exist: pip3 freeze --local requirements.txt echo web: python app.py > Procfile
Create Heroku App, Select Postgres add-on, download Heroku CLI toolbelt, login to heroku (Heroku login), git init, connect git to heroku (heroku git remote -a ), git add ., git commit, git push heroku master.
heroku ps:scale web=1
In heroku app settings set the config vars to add DATABASE_URL, IP and PORT
Credits
Jordan Daly - This project was completed as part of Code Institute’s Mentored Online Full Stack Web Development course in 2018.

Content
The content for recipes was taken from the BBC recipes website.

Media
The images for recipes were also taken from the BBC recipes website.

Acknowledgements
Image upload to AWS S3 with boto3 info from this blog. Unit testing strategy from this blog.

