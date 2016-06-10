import os

base_dir = os.path.abspath(os.path.dirname(__file__))


DATABASE_NAME = 'movedb'
DEBUG = True


MAIL_SERVER = 'smtp.volstelecom.ru'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = 'shop@volstelecom.ru'
MAIL_PASSWORD = 'j8njeRca'
MAIL_SENDER = 'VOLStelecom shop <shop@volstelecom.ru>'
MAIL_MANAGER = 'dkurkov@volstelecom.ru'
#MAIL_MANAGER = 'elukashin@volstelecom.ru'
#MAIL_USERNAME = os.environ.get('MAIL_USERNAME')