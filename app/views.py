from flask import Flask, render_template, jsonify
from app import app
import sqlite3 as sql

DATABASE_NAME = 'shop.db'

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

@app.route('/equipments')
def equipments():
	return render_template('equipments.html')

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
	print(len(level))
	return render_template('passivnieComponentiVols.html')