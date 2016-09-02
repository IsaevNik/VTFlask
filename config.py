import os

base_dir = os.path.abspath(os.path.dirname(__file__))

DATABASE_NAME = 'movedb'
DEBUG = True

MAIL_SERVER = 'smtp.volstelecom.ru'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
DATABASE_USER = 'volstelecom'
DATABASE_PASSWORD = 'fF1NWg'
MAIL_SENDER = 'VOLStelecom shop <shop@volstelecom.ru>'
MAIL_MANAGER = 'kooperative@mail.ru'
#MAIL_MANAGER = 'elukashin@volstelecom.ru'
#MAIL_MANAGER = 'dkurkov@volstelecom.ru'
