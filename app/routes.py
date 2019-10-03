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
	session.auth = ('RUGAlbert', '295ff5127f047fc96542a37253b67f94bcf614b4')
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
	return render_template("searchresults.html", users=usersData)
