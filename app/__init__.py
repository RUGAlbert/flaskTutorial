from flask import Flask, session
from flask import render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
rootDir = os.path.dirname(os.path.abspath(__file__))


from app import routes

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', title='Error', error=404), 404
	
	
