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
```python
from app import routes
```
This is enough for the app to understand where to find the routes.
So let's create our first route.
#### **`app/routes.py`**
```python
from app import app

@app.route('/')
def home():
	return "Hellllllloooo world"
```

Again we have to import the app so we can define routes.
With  ```@app.route('/')``` we say that if you go towards http://localhost:8000/ we see this 'page'.
Now you got your first fully working flask app.

## Extending hello world
But if you now go towards http://localhost:8000/search-users what happens? Indeed an ugly errorpage. So before going on lets fix that first. Since it is very important to let users know what is happening.
So inside the app directory we add a new folder templates.
This are all the jinja2 html pages we are going to use.
Inside the templates folder we are going to add a new folder called errors. Today we are only go to use it for one error page, but normally you have more. Copy the file 404.html from the source. We are not going to discuss how to create html and css pages. However we are going to discuss how to create a template:

#### **`app/templates/errors/404.html`**
```html
{% extends 'bootstrap/base.html' %}

{% block title %}
	{% if title %}
		{{ title }} - Flask Tutorial
	{% else %}
		Flask Tutorial
	{% endif %}
{% endblock %}
```

If you know a bit about html you probably already saw that this isn't a normal html page. This is a template, the server side does some processing before serving it to the client. 
So the first line says that it is using bootstrap. This means that we can build forward on that template and use bootstrap classes. For the people who have never heard about bootstrap before, it is a library consisting of mainly css files to make it easier to create a good looking front-end. 
Then a block starts, this is an object defined by the parent (the file it extends from). For example title, which defines the title of website.
In this we do an if statement (logic is done by using {% %}. And if a title is defined we will use that, otherwise we will just use a default.  The {{ }} say that inside this some variable is used, or some function is called which will return something to be used inside that bit of the html page. For example the title.

#### **`app/templates/errors/404.html`**
```html
...
{% block styles %}
{{ super() }}
<link rel="stylesheet" href="{{url_for('.static', filename='styles/404.css', version=config['VERSION'])}}">
{% endblock %}
```
It the styles block we first state that we want to use every style it is extending from (so the bootstrap style files). 
The next line imports a css file you have created, more about this later once we created the file itself. Now more about the syntax. So everything is html except the href. So let's see how that works. We use the function url_for(routeName, *functionParameters, *queryParameter). Flask already got the route .static defined. They are all the files inside the static folder,  this means that it is loaded and then cached. So we have to make sure if we have a new version it is updated. A route can have parameters, for now just accept that, later on in this tutorial we will actually create a route with parameters so you know how to do that. This function has one parameter namely the filename, which is in our case styles/404.css. We only have one last parameter, version. This is a dummy query parameter (remember a query parameter is defined like this ```www.url.com/an/awesome/url?<name>=<value>```. Now every time we have a new css file, we can update the version and it will reload it's cache. Since the browser sees this as a different file. 
Now there is only one question, how do we know the version of the file without hardcoding it. It will postpone that for just a few minutes.
Let's first finish this html page.

#### **`app/templates/errors/404.html`**
```html
{% block content %}
<section class="page_404">
	<div class="container">
		<div class="row">	
			<div class="col-sm-12 ">
				<div class="col-sm-10 col-sm-offset-1  text-center">
					<div class="four_zero_four_bg">
						<h1 class="text-center ">404</h1>
					</div>
					
					<div class="contant_box_404">
						<h3 class="h2">
							Look like you're lost
						</h3>
						
						<p>the page you are looking for not avaible!</p>
						
						<a href="/" class="link_404">Go to Home</a>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>
{% endblock %}
```
So the whole html part is not interesting for this tutorial. This leaves us with the block content, which as you might have guessed is the body of the html page.
So know we have the 404 page, except we don't have the css file and the version control still has to be defined somewhere.
Let's start with the css file, since that is the easiest. Again just copy this from the source code and place it in /static/styles/404.css
Everything that is within the static folder, will automatically be cached by the client. (At least if it is using a default browser like chrome).
Now the last part the version control.
For all the default parameters for this app we are going to create a new file called config.py.
#### **`config.py`**
```python
import os

class Config(object):
    VERSION = '0.1.0'
    ISDEBUG = (os.environ.get('ISDEBUG', 'True') == 'True')
```
As you can see we defined only 3 variables within this class. 
First of all, normally you would define something like a secret key, but that is out of the scope of this tutorial. 
We have a version variable, used for *wait for it* version control. And a ISDEBUG parameter which is used to determine if you are currently running a debug server. You can use this above print statements to make sure that in a production server that is not printed.

We have this file now, but of course flask still needs to understand where to find it.
So we are going to update our init file.
#### **`app/__init__.py`**
```python
from flask import Flask, session
from flask import render_template
from config import Config
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config.from_object(Config)


from app import routes

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', title='Error'), 404
```

As you can see we now import the config file, then init the config for the app.

And create an errorhandler 
```@app.errorhandler(404)``` states that whenever the error 404 is thrown this function is run.
So the function has as parameter info about the error, which we currently are not going to use.
And we return the result of render_template()
This function takes the template we just defined, and makes a html file out of it. The first parameter defines the template used. All the others parameters used within template. In this template only the title parameter. Which we will name error. We also return as statuscode 404. This is important since it is the norm to also return the status itself.

Now you got a fully working flask app, including basic error handling.
