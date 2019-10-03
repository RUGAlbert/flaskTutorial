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
It the styles block we first state that we want to use every style it is extending from (so the bootstrap style files). That means super(). If you programmed in an OOP  language, this might look familiar.
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
#### **`/static/styles/404.css`**
```css
.page_404{ 
	padding:40px 0; 
	background:#fff; 
	font-family: 'Arvo', serif;
}

.page_404  img{ 
	width:100%;
}

.four_zero_four_bg{
	background-image: url(https://cdn.dribbble.com/users/285475/screenshots/2083086/dribbble_1.gif);
	height: 400px;
	background-position: center;
}
 
 
.four_zero_four_bg h1{
	font-size:80px;
}
 
.four_zero_four_bg h3{
	font-size:80px;
}

.link_404{			 
	color: #fff!important;
	padding: 10px 20px;
	background: #39ac31;
	margin: 20px 0;
	display: inline-block;
}

.contant_box_404{ 
	margin-top:-50px;
}
```
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

## Real application

So basically you already now know how to build a full flask app.
But since this isn't much fun we are going to add a github user search to our website.
So we start with 2 html pages I just found online somewhere and put them in 2 different files. 
And also add the css files
We are going to change a bit of it. 
css files:
#### **`app/static/styles/searchresults.css`**
```css
@import "http://fonts.googleapis.com/css?family=Roboto:300,400,500,700";

.container { 
	margin-top: 20px; 
} 
.mb20 { 
	margin-bottom: 20px; 
}  

hgroup { 
	padding-left: 15px; 
	border-bottom: 1px solid #ccc; 
} 
hgroup h1 { 
	font: 500 normal 1.625em "Roboto",Arial,Verdana,sans-serif; 
	color: #2a3644; 
	margin-top: 0; 
	line-height: 1.15; 
} 
hgroup h2.lead { 
	font: normal normal 1.125em "Roboto",Arial,Verdana,sans-serif; 
	color: #2a3644; 
	margin: 0; 
	padding-bottom: 10px; 
} 

.search-result .thumbnail { 
	border-radius: 0 !important; 
} 

.search-result:first-child { 
	margin-top: 0 !important; 
}
 
.search-result { 
	margin-top: 20px; 
}
 
.search-result .col-md-2 { 
	border-right: 1px dotted #ccc; 
	min-height: 140px; 
}
 
.search-result ul { 
	padding-left: 0 !important; 
	list-style: none;  
} 

.search-result ul li { 
	font: 400 normal .85em "Roboto",Arial,Verdana,sans-serif;  
	line-height: 30px; 
} 

.search-result ul li i { 
	padding-right: 5px; 
} 

.search-result .col-md-7 { 
	position: relative; 
}
 
.search-result h3 { 
	font: 500 normal 1.375em "Roboto",Arial,Verdana,sans-serif; 
	margin-top: 0 !important; 
	margin-bottom: 10px !important; 
}
 
.search-result h3 > a, .search-result i { 
	color: #353b48 !important; 
}
 
.search-result p { 
	font: normal normal 1.125em "Roboto",Arial,Verdana,sans-serif; 
}  

.search-result span.plus { 
	position: absolute; 
	right: 0; 
	top: 126px; 
}
 
.search-result span.plus a { 
	background-color: #353b48; 
	padding: 5px 5px 3px 5px; 
}
 
.search-result span.plus a:hover { 
	background-color: #414141; 
}
 
.search-result span.plus a i { 
	color: #fff !important; 
}
 
.search-result span.border { 
	display: block; 
	width: 97%; 
	margin: 0 15px; 
	border-bottom: 1px dotted #ccc; 
} 
```

#### **`app/static/styles/search.css`**
```css

body,html{
    height: 100%;
    width: 100%;
    margin: 0;
    padding: 0;
    background: #e74c3c !important;
}

.searchbar{
    margin-bottom: auto;
    margin-top: auto;
    height: 60px;
    background-color: #353b48;
    border-radius: 30px;
    padding: 10px;
}

.search_input{
    color: white;
    border: 0;
    outline: 0;
    background: none;
    width: 0;
    caret-color:transparent;
    line-height: 40px;
    transition: width 0.4s linear;
}

.searchbar:hover > .search_input, .search_input.hovered{
    padding: 0 10px;
    width: 450px;
    caret-color:red;
    transition: width 0.4s linear;
}

.searchbar:hover > .search_icon, .search_icon.hovered{
    background: white;
    color: #e74c3c;
}

.search_icon{
    height: 40px;
    width: 40px;
    float: right;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    color:white;
}

.searchbarfull{
	height: 100%;
}

.searchresults{
	height: 10%;
	transition:height 0.4s linear;
}
```

Now for the html pages it goes a little bit differently.
So first the search page:
#### **`app/templates/search.html`**
```html
{% extends 'searchbase.html' %}

{% block searchquery %}
<div class="container searchbarfull">
  <div class="d-flex justify-content-center h-100">
	<div class="searchbar">
	  <input id="input" class="search_input" type="text" name="" placeholder="Search...">
	  <a href="#" class="search_icon"><i class="fas fa-search"></i></a>
	</div>
  </div>
</div>
{% endblock %}
```

Again there is some html, which we will not discuss. But it is inside a block called searchquery. This will be defined just in a second. Since it is a block defined in the searchbase template, which we will discuss shortly.

So how does the searchbase.html template look like?
#### **`app/templates/searchbase.html`**
```html
{% extends 'bootstrap/base.html' %}

{% block title %}
	{% if title %}
		{{ title }} - Flask Tutorial
	{% else %}
		Flask Tutorial
	{% endif %}
{% endblock %}

{% block scripts %}
{{super()}}
<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script>
	$('#input').keypress(function (e) {
		if (e.which == 13) {
			var search = $(this).val();
			$(this).addClass("hovered");
			$(".searchbarfull").addClass("searchresults");
			window.location.href = "{{url_for('userSearchQuery', query='')}}"+search;
			return false;
		}
	});
</script>
{% endblock %}

{% block styles %}
{{ super() }}
<link rel="stylesheet" href="{{url_for('.static', filename='styles/search.css', version=config['VERSION'])}}">
<link rel="stylesheet" href="{{url_for('.static', filename='styles/searchresults.css', version=config['VERSION'])}}">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
{% endblock %}

{% block content %}

{% block searchquery %}
{% endblock %}

{% block searchresults %}
{% endblock %}

{% endblock %}
```

The extends and title part are already explained, so I will skip that part.
Furthermore since this is a flask tutorial and we already discussed links and so on, generated by jinja2 we will skip explaining that.
Just realize that the styles and scripts block start with a super().
For the scripting part, what it does, it checks if you press enter when you are typing inside the searchbox, if so it will start the css animation and go to the correct link using the url_for function.

The interesting part is the content block. we only have 4 lines inside it. What we do here is define a block which can later be filled in by a template which extends on this page. Which we did on the search template. What we now can do is create the last template which is the searchresults page. Since we already got the base done we hardly have to code anything new.

#### **`app/templates/searchresults.html`**
```html
{% extends 'searchbase.html' %}

{% block searchquery %}
<div class="container searchbarfull searchresults">
  <div class="d-flex justify-content-center h-100">
	<div class="searchbar">
	  <input id="input" class="search_input hovered" type="text" name="" placeholder="Search...">
	  <a href="#" class="search_icon"><i class="fas fa-search"></i></a>
	</div>
  </div>
</div>
{% endblock %}

{% block searchresults %}
<div class="container">
	<section class="col-xs-12 col-sm-6 col-md-12">
		{% for u in users %}
			<article class="search-result row">
				<div class="col-xs-12 col-sm-12 col-md-3">
					<a href="#" title="avatar" class="thumbnail"><img src="{{u.avatar_url}}" alt="avatar" /></a>
				</div>
				<div class="col-xs-12 col-sm-12 col-md-2">
					<ul class="meta-search">
						<li><i class="glyphicon glyphicon-calendar"></i> <span>{{u.created_at}}</span></li>
						<li><i class="glyphicon glyphicon-time"></i> <span>{{u.updated_at}}</span></li>
						<li><i class="glyphicon glyphicon-tags"></i> <span>{{u.public_repos}}</span></li>
					</ul>
				</div>
				<div class="col-xs-12 col-sm-12 col-md-7 excerpet">
					<h3><a href="#" title="">{{u.name}}</a></h3>
					<p>{{u.bio}}</p>	
				</div>
				<span class="clearfix borda"></span>
			</article>
		{% endfor %}
	</section>
</div>
{% endblock %}

```

As you can see we now use both the blocks. The first block might look exactly the same, but we added the class searchresults and hovered to the divs, which make sure the animation is already played and done on this page.

The second block is more interesting.
As you might see there is a for loop inside it. And for every user in the list it will create that part of the html. With of course different values for the avatar and so on.

So last but not least we have to add this towards the routes page.
So the new routes.py becomes:
#### **`app/routes.py`**
```python
from app import app
from flask import render_template, jsonify
import requests
import os

@app.route('/')
def home():
	return "You have found home"

@app.route('/users-search')
def userSearch():
	return render_template("search.html")

@app.route('/users-search/<query>')
def userSearchQuery(query):
	session = requests.Session()
	session.auth = ('RUGAlbert', 'token')
	r = session.get('https://api.github.com/search/users?q='+query)
	users = r.json()['items']
	usersData = []
	for u in users[1:10]:
		newUser = {}
		newUser['avatar_url'] = u['avatar_url']
		newUser['name'] = u['login']
		userR = session.get(u['url'])
		userJson = userR.json()
		newUser['bio'] = userJson['bio']
		newUser['created_at'] = userJson['created_at']
		newUser['updated_at'] = userJson['updated_at']
		newUser['public_repos'] = userJson['public_repos']
		usersData.append(newUser)
	return render_template("searchresults.html", title=query, users=usersData)
```

So first things first, the 
```python
@app.route('/users-search')
def userSearch():
	return render_template("search.html")
```

States that whenever you come to this route you will get the rendered template of search.html, nothing special. The other route is way more special.

So we already discussed the for loop in the template, but where does this data come from.
From an api call to github.

```python
@app.route('/users-search/<query>')
def userSearchQuery(query):
```
But first the route looks a bit different than normal. inside the url we have <>. This means we specify a parameter. In this case the search query. Please note that normally this is not the way to implement a search (it would make more sense to put it inside the parameters of an url), but for the sake of this tutorial we are going to implement it this way.
So now we get what the parameter is.
Inside python there is a nice requests library which will do all the hard word for us.
So we start with creating a session, because we need to authenticate with something. Then we will search using the query and loop trough the first 10 results. The reason is that I don't pay for github and only have a limmited number of api calls I can make, so I use it to make sure I will not burn trough all the api request that I'm allowed to do every day within one search. In userData we will at the end put all our results.

```python
session = requests.Session()
session.auth = ('RUGAlbert', 'token')
r = session.get('https://api.github.com/search/users?q='+query)
users = r.json()['items']
usersData = []
for u in users[1:10]:
```
Even though this already got a lot of info we want a bit more, for example the day they created their account and their bio.
So let's implement that:
```python
newUser = {}
newUser['avatar_url'] = u['avatar_url']
newUser['name'] = u['login']
userR = session.get(u['url'])
userJson = userR.json()
newUser['bio'] = userJson['bio']
newUser['created_at'] = userJson['created_at']
newUser['updated_at'] = userJson['updated_at']
newUser['public_repos'] = userJson['public_repos']
usersData.append(newUser)
```

So we first create a new dict, and put inside it all the info we already know, then we do a new get request with the url provided trough the api. And get some more data about that.
At the end we append it to the list.

Now we only have to render the template.
```python
return render_template("searchresults.html", title=query, users=usersData)
```
so we render the html page, which we already knew, we give a title. Note that I'm using the query the user had searched for and also pass the data for the for loop.

And here you have it, an awesome page.

## Extra stuff

Since I did not write any api by myself, we will now create a very simple api. Just to be clear the functions 'insertData()' and 'getData()' do not really excist, you should define them for your own.

### Get data
```python
from flask import request, jsonify
@app.route('/api/search-users', methods=["GET"])
def getUsers():
	#gets the data from the request (search query for example)
	username = request.args.get('username')
	result = getData(username)
	return jsonify(result)
```

### Put data
```python
from flask import request, jsonify
@app.route('/api/users', methods=["PUT"])
def getUsers():
	#gets the data from the request
	username = request.args.get('username')
	result = insertData(username)
	#note the 201 we return to indicate a correct insert
	return jsonify(result), 201
```
