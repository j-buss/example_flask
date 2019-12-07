# Deploying Flask Apps into Google Cloud Platform

There are many Flask tutorials online that describe the details of using the lightweight Python framework.pyi
With this series I do not intend to recreate the great jobs that have been done.
I simply wanted a quick (2 or 3) post series to get up and running with deploying Flask to
GCP App Engine and using data from Big Query.


## Part 1: Creating Your First Flask App

Let's take a simple Flask app and make certain that we can deploy it to GCP. Essentially we will take the "5-line minimum" 
and add a few other items to be able to deploy it to GCP App Engine.

### 1. Minimum app tested locally:
Install Flask:
```bash
pip install flask
```
Create the "5-line minimum" app.py file:  
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```
That file is the only code we need. However we need to 
 ```bash
export FLASK_APP=app.py
flask run
* Running on http://127.0.0.1:5000/
 ```
Run the app:

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
### Resources:
#### Tutorials
- [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
 : The Flask Tutorial Gold Standard. In a clear and consistent format it walks you through all the basics and well into the intermediate range.
 Not only that, but the tutorial is a delight to work through. 
 The author Miguel Grinberg writes in a way that it is a pleasure to follow along. 
 His love of Flask and Python are evident.
- [Your First Flask App](https://hackersandslackers.com/your-first-flask-application/) is a series of posts which describe many facets of Flask.
The series includes blueprints, Jinja and SQLAlchemy. It is not intended to be a step-by-step tutorial, but instead describes the concepts in a very 
conversational way.
- [Deploying a Python Flask Web Application to App Engine Flexible](https://codelabs.developers.google.com/codelabs/cloud-vision-app-engine/index.html?index=..%2F..index#0)
is a Google Cloud Codelabs walk-through describing each of the steps to deploy a vision app from Google's Github repository: 
[python-docs-sample](https://github.com/GoogleCloudPlatform/python-docs-samples) 

#### Podcast:
- [Building Flask-based Web Apps](https://talkpython.fm/episodes/show/48/building-flask-based-web-apps) is a podcast interview on [Talk Python to Me]()
