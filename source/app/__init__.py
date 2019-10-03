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
	
	
