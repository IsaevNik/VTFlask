from flask.ext.mail import Message
from threading import Thread

from app import mail
from app import app

def send_async_email(msg):
	with app.app_context():
		mail.send(msg)


def send_message(to, subject, body):
	msg = Message(subject, sender=app.config['MAIL_SENDER'], recipients=[to])
	msg.body = body
	thr = Thread(target = send_async_email, args = [msg])
	thr.start()