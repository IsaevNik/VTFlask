from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask.ext.mail import Mail, Message
import json
from app import app
import sqlite3 as sql
import os
import codecs

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'isv.nikita@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_SENDER'] = 'VOLStelecom shop <volstelecomshop@gmail.com>'
app.config['MAIL_MANAGER'] = 'kooperative@mail.ru'


mail = Mail(app)
base_dir = os.path.abspath(os.path.dirname(__file__))
DATABASE_NAME = os.path.join(base_dir,'shop.db')

def get_table(name):
	result = {}
	with sql.connect(DATABASE_NAME) as con:
		cur = con.cursor()
		cur.execute('SELECT DISTINCT type FROM {}'.format(name))
		result = {res[0]:[] for res in cur.fetchall()}
		for k in result.keys():
			cur.execute('SELECT * FROM {} WHERE type = ?'.format(name),(k,))
			items = [{'id':item[0],'name':item[1],'price':item[2],'img':item[3]} for item in cur.fetchall()]
			result[k] = items
	return result

def send_message(to, subject, body):
	msg = Message(subject, sender=app.config['MAIL_SENDER'], recipients=[to])
	msg.body = body
	mail.send(msg)

@app.route('/')
def index():
	return(render_template('index.html'))


@app.route('/main_page')
def main_page():
	return render_template('main_page.html')

@app.route('/our_clients')
def our_clients():
	return render_template('our_clients.html')

@app.route('/services')
def services():
	return render_template('services.html')

@app.route('/equipments', methods=['GET','POST'])
def equipments():
	if request.method == 'GET':
		return render_template('equipments.html')
	else:
		data = request.get_json()
		client_name = data["client_name"]
		client_telephon = data["client_telephon"]
		client_email = data["client_email"]
		client_comment = data["client_comment"]
		items = data["items"]
		msg = u'{:+^50}\n'.format(' New request ')
		msg += u'name: {} \ntelephone: {} \nemail: {} \ncomment: "{}" \n'.format(client_name, client_telephon, client_email, client_comment)
		msg += '+'*50;
		msg += "\nClients request: \n"
		msg += '+'*50;
		for item in items:
			msg += u'\n{name_of_item} \ncount: {count}\n'.format(**item)
			msg += '-'*50
		send_message(app.config['MAIL_MANAGER'], "new request", msg)
		return '/equipments'

@app.route('/certificates')
def certificates():
	return render_template('certificates.html')

@app.route('/contacts')
def contacts():
	return render_template('contacts.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/passivnieComponentiVols')
def passivnieComponentiVols():
	level = get_table('PassivnyeKomponentyVols')
	return render_template('level_base.html', level=level)

@app.route('/krossOpticheskiy')
def krossOpticheskiy():
	level = get_table('KrossOpticheskiy')
	return render_template('level_base.html', level=level)

@app.route('/muftaOpticheskaya')
def muftaOpticheskaya():
	level = get_table('MuftaOpticheskaya')
	return render_template('level_base.html', level=level)

@app.route('/instrumentDlyaRazdelkiVols')
def instrumentDlyaRazdelkiVols():
	level = get_table('InstrumentDlyaRazdelkiVols')
	return render_template('level_base.html', level=level)

@app.route('/diagnostikaVols')
def diagnostikaVols():
	level = get_table('DiagnostikaVols')
	return render_template('level_base.html', level=level)

@app.route('/svarochnyeApparaty')
def svarochnyeApparaty():
	level = get_table('SvarochnyeApparaty')
	return render_template('level_base.html', level=level)

@app.route('/reflektometrOpticheskiy')
def reflektometrOpticheskiy():
	level = get_table('ReflektometrOpticheskiy')
	return render_template('level_base.html', level=level)

@app.route('/rashodnyeMaterialy')
def rashodnyeMaterialy():
	level = get_table('RashodnyeMaterialy')
	return render_template('level_base.html', level=level)

@app.route('/dopolnitelnoeOborudovanie')
def dopolnitelnoeOborudovanie():
	level = get_table('DopolnitelnoeOborudovanie')
	return render_template('level_base.html', level=level)

@app.route('/patchKordyOpticheskie')
def patchKordyOpticheskie():
	level = get_table('PatchKordyOpticheskie')
	level.pop(u'%u041F%u0430%u0442%u0447%20%u043A%u043E%u0440%u0434%u044B%20%u043E%u043F%u0442%u0438%u0447%u0435%u0441%u043A%u0438%u0435', None)
	return render_template('level_base.html', level=level)

@app.route('/shkafyIStoiki')
def shkafyIStoiki():
	level = get_table('ShkafyIStoiki')
	return render_template('level_base.html', level=level)

@app.route('/opticheskieKonnektory')
def opticheskieKonnektory():
	level = get_table('OpticheskieKonnektory')
	return render_template('level_base.html', level=level)

@app.route('/kabelnyeSborki')
def kabelnyeSborki():
	level = get_table('KabelnyeSborki')
	return render_template('level_base.html', level=level)