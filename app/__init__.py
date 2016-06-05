from flask import Flask
from flask.ext.mail import Mail
from peewee import *

from errors import file_handler


app = Flask(__name__)
app.config.from_object('config')
if not app.config['DEBUG']:
	app.logger.addHandler(file_handler)
db = MySQLDatabase(app.config['DATABASE_NAME'], **{'password': '1234', 'user': 'root'})
mail = Mail(app)


from app import views