## Part 1: Creating Your First Flask App 

Create the 5 line hello World app.py
 - Run from command line
 ```python
    export FLASK_APP=app.py
    flask run
    * Running on http://127.0.0.1:5000/
 ```
 https://flask.palletsprojects.com/en/1.1.x/quickstart/
 - deploy to gcp
    create the app.yaml file
    ```python
    runtime: python37
    ```
    gcloud config set project [PROJECT_NAME]
    enable cloud build api

    gcloud app deploy
 -