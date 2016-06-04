# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
import os
import codecs
from collections import OrderedDict

from models import Shop
from emails import send_message
from app import app
from config import base_dir

def get_level(name):
	result = OrderedDict({})
	for sublvl in (Shop
				.select(Shop.sublevel)
				.distinct()
				.order_by(Shop.sublevel)
				.where(Shop.level == name)):

		sublevel_name = sublvl.sublevel
		result[sublevel_name] = []

		for line in (Shop
					.select()
					.order_by(Shop.name)
					.where(Shop.sublevel == sublevel_name)):

			item = ({'name' : line.name, 
					 'price' : line.price / 1.00,
					 'img' : 'shop/foto/' + str(line.foto) + '.jpg', 
					 'description' : line.description})
			img_path = os.path.join(base_dir,'app', 'static', 'shop', 'foto', str(line.foto) + '.jpg')
			if not os.path.exists(img_path):
				item['img'] = 'shop/foto/0000.jpg'
			result[sublevel_name].append(item)

	return result

def make_message(data):
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
	return msg

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
		msg = make_message(data)
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
	level = get_level('Пассивные компоненты ВОЛС')
	return render_template('level_base.html', level=level)

@app.route('/electrica')
def electrica():
	level = get_level('Электрика')
	return render_template('level_base.html', level=level)

@app.route('/montagiIzmereniya')
def montagiIzmereniya():
	level = get_level('Монтаж и измерения оптических линий связи')
	return render_template('level_base.html', level=level)