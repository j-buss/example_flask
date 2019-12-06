# Deploying Flask Apps to GCP
## Part 1: Creating Your First Flask App

There are many Flask tutorials online that describe the details of using the lightweight Python framework.pyi
With this series I do not intend to recreate the great jobs that have been done.
I simply wanted a quick (2 or 3) post series to get up and running with deploying Flask to
GCP App Engine and using data from Big Query.

### Resources:
1. [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
by Miguel Grinberg is a phenominal tutorial for Flask. Not just the basics, but some pretty
in-depth concepts.
- In a related note there is a great podcast interview with Miguel on
[Talk Python to Me](https://talkpython.fm/) where he discusses [Building Flask-based Web Apps](https://talkpython.fm/episodes/show/48/building-flask-based-web-apps)
2. [Your First Flask App](https://hackersandslackers.com/your-first-flask-application/) is a series of posts which describe many facets of Flask.
The depth does not go to the step-by-step that Miguel does, however contains in his tutorial, but is very good. 
3. GCP Examples

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