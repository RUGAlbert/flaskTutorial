# Flask Tutorial

## Introduction
Before we start we this tutorial please note that this is not about the best structure for you flask app. This is mainly build to have an introduction to flask. Keep that in mind while using this.
Moreover we are just going to focus on a development server and not also a production server.
This file assumes you are using linux.

There are 2 folders, the folder in which everything works and sometimes during the tutorial you have to copy from and an almost empty folder your work folder.

Before we start we first have to install python 3.x, and python3 virtual environment.  After installing this in your preferred way, we first are going to create a python virtual environment. You can find the start folder in this github project. Create the environment by using the following command 
```
python3 -m venv env
```
And go inside the environment with 
```
source env/bin/activate
```
More info can be found here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

Install all needed dependencies with
```
pip install -r requirements.txt
```
Now we can really start with working with flask.

## 'Hello Globe'

To kick this off we ofcourse are going to create a hello world working example.
First off we create a new file called 'startServer.py'. This is the script that will be used to start the server.
#### **`startServer.py`**
```python
from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, threaded=True)
```
So this means that flask will run the app on all available public ip addresses on this computer with port 8000. Also the threading is enabled to allow for parallel handling of requests. 

Also we import from app, app. What is this app? It is something we have not defined yet.
So we are going to add a folder called app and create a file inside that folder called '_ _ init _ _.py' (without spaces). 

#### **`app/__init__.py`**
``` python
from flask import Flask, session
from flask import render_template
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

#from app import routes
```

We are first going to focus on the uncommented lines of the code.
The first lines a some imports and I assume you already understand how that works.  Then we create  the flask app itself. Moreover we also install bootstrap to the app. 

Basically we now have a working app which is useless.
So we have to add a route. Before starting adding routes we first have to make the app understand where to find it. You can do so by uncommenting the line 
```
from app import routes
```
This is enough for the app to understand where to find the routes.
So let's create our first route.
#### **`app/routes.py`**
```
from app import app

@app.route('/')
def home():
	return "Hellllllloooo world"
```

Again we have to import the app so we can define routes.
With  ```@app.route('/')``` we say that if you go towards http://localhost:8000/ we see this 'page'.
Now you got your first fully working flask app.
