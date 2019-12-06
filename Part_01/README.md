# Part 1: Creating Your First Flask App

This post is about running a hello world app in Flask and then in Google Cloud Platform's tool App Engine.

Within the post
Create the 5 line hello World app.py
 - Run from command line
 ```python
    export FLASK_APP=app.py
    flask run
    * Running on http://127.0.0.1:5000/
 ```
 https://flask.palletsprojects.com/en/1.1.x/quickstart/
 - deploy to gcp
    rename app.py to main.py
    - without a module named main it will error out....
    - cp app.py as main.py

    create the app.yaml file
    ```python
    runtime: python37

    ```
    gcloud config set project [PROJECT_NAME]
    enable cloud build api

    gcloud app deploy
 -