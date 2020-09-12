# ProjectGames
Project Level2
World of Games

Notes:
The default application (docker) URL address is http://192.168.99.102
You can change the URL application via /Tests/application_URLtxt

e2e.py
This file will have two functions.

Functions
1. test_scores_service(app_url) – Will test our web service.
Will get the application URL as an input, open a browser to that URL, select the score
element in our web page, check that it is a number between 0 to 1000 and return a
boolean value if it’s true or not.
2. main_function() –
Will call our tests function.
The main function will return -1 as an OS exit code if the tests failed and 0 if it passed.

Dockerfile
The Dockerfile will do the below steps:
 Package the project
 Package Scores.txt
 Install pip dependencies
 Run MainScores.py (set it in the CMD block).

Docker-compose.yml
This file will be used to manage our application.
It will be used to build the application (built by the Dockerfile) and run it.

Jenkinsfile
This will consist the jenkins pipeline which will contain the following stages:
1. Checkout - checkout the repository (containing the project).
2. Build - Build our docker image.
3. Run - will run our dockerized application and will expose it to port 5000 on localhost.
4. Test - e2e.py module it will perform a selenium test on the “scores web service” and fail
the pipeline if the tests failed.
5. Finalize - Will terminate our tested container

Scores.txt
Will have an initial value of 0
