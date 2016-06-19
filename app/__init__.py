from flask import Flask
from flask.ext.mail import Mail
from peewee import *
from werkzeug.contrib.fixers import ProxyFix


from errors import file_handler


app = Flask(__name__)
app.config.from_object('config')
app.wsgi_app = ProxyFix(app.wsgi_app)

if not app.config['DEBUG']:
	app.logger.addHandler(file_handler)

db = MySQLDatabase(app.config['DATABASE_NAME'], 
		**{'password': app.config['DATABASE_PASSWORD'], 
		   'user': app.config['DATABASE_USER']})

mail = Mail(app)
from app import views
