from flask import Flask
from flask.ext.mail import Mail
from peewee import *

app = Flask(__name__)
app.config.from_object('config')
db = MySQLDatabase('movedb', **{'password': '1234', 'user': 'root'})
mail = Mail(app)

from app import views