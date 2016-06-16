# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
import os
import codecs
from collections import OrderedDict
from peewee import DoesNotExist
import re

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
					 'price' : line.price,
					 'img' : 'shop/foto/' + str(line.foto) + '.jpg', 
					 'description' : line.description})
			img_path = os.path.join(base_dir,
									'app', 
									'static', 
									'shop', 
									'foto', 
									str(line.foto) + '.jpg')
			if not os.path.exists(img_path):
				item['img'] = 'shop/foto/0000.jpg'
			result[sublevel_name].append(item)

	return result


def search_on_db(text):
	result = {}
	try:
		Shop.get(Shop.name.contains(text))
	except DoesNotExist:
		result['not found'] = True
	else:
		result[u'Результат поиска'] = []
		for line in Shop.select().where(Shop.name.contains(text)):
			item = ({'name' : line.name, 'price' : line.price,
					 'img' : 'shop/foto/' + str(line.foto) + '.jpg', 
					 'description' : line.description})
			img_path = os.path.join(base_dir,
									'app', 
									'static', 
									'shop', 
									'foto', 
									str(line.foto) + '.jpg')

			if not os.path.exists(img_path):
				item['img'] = 'shop/foto/0000.jpg'
			result[u'Результат поиска'].append(item)
	return result


def make_message(data):
	client_name = data["client_name"]
	client_telephon = data["client_telephon"]
	client_email = data["client_email"]
	client_comment = data["client_comment"]
	items = data["items"]
	msg = u'{:+^50}\n'.format(' New request ')
	msg += u'name: {} \ntelephone: {} \nemail: {} \ncomment: "{}" \n'.format(
												client_name, 
												client_telephon, 
												client_email, 
												client_comment)
	msg += '+'*50;
	msg += "\nClients request: \n"
	msg += '+'*50;
	for item in items:
		msg += u'\n{name_of_item} \ncount: {count}\n'.format(**item)
		msg += '-'*50
	return msg


def get_name(name):
	if name.startswith(u'Коннектор'):
		result = re.search(r' (.*)-[SM]M', name)
		return result.groups()[0]
	else:
		return ' '.join(name.split()[5:-1])


def get_data_for_calculator():
	list_of_types = {name.calculator : [] for name in (Shop
											   .select(Shop.calculator)
											   .distinct()
											   .where(Shop.calculator.is_null(False)))}
	for item in list_of_types.keys():
		list_of_types[item] = [{'name': get_name(product.name), 
								'price': product.price} 
									for product in (Shop
												   .select(Shop.name, Shop.price)
												   .where(Shop.calculator == item))]
	return list_of_types


def get_price_of_component(name):
	try:
		line = Shop.get(Shop.name.contains(name))
	except DoesNotExist:
		abort(500)
	else:
		return line.price


def get_price_of_patch(cab_len, con_l, con_r, cab_n, cab_t):
	price = 0.0;
	if cab_t == 'duplex':
		k = 2;
	else:
		k = 1;

	if cab_len < 1:
		cab_len = 1
	
	price += k * get_price_of_component(con_l)
	price += k * get_price_of_component(con_r)
	price += cab_len * get_price_of_component(cab_n)

	return '{:.2f}'.format(price)


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

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


@app.route('/getlevel', methods=['GET','POST'])
def getlevel():
	if request.method == 'GET':
		return abort(404)

	level_name = request.get_json().get("page")
	level = get_level(level_name)

	if level_name == u'Патч-корды':
		data_for_calc = get_data_for_calculator() 
		return render_template('level_patch.html', level=level, 
												   calc=data_for_calc)
	return render_template('level_base.html', level=level)

@app.route('/search', methods=['POST'])
def search():
	userRequest = request.get_json()
	level = search_on_db(userRequest['text'])
	return render_template('level_base.html', level=level)

@app.route('/calculatepatch', methods=['POST'])
def calculatepatch():
	userPatch = request.get_json()
	connectorLeft = userPatch['connectorLeft']
	connectorRight = userPatch['connectorRight']
	mod = userPatch['mod']
	diametr = userPatch['diametr']
	cabel_type = userPatch['typeConnection']
	connector_left_name = '-'.join([
		connectorLeft,
		mod,
		diametr
		]) + u'мм'
	connector_right_name = '-'.join([
		connectorRight,
		mod,
		diametr
		]) + u'мм'
	cabel_name = u'{}мм {}, {}'.format(diametr,
									   cabel_type,
									   userPatch['typeCabel'].split(' --- ')[0])
	cabel_lenght = float(userPatch['lenghtCabel'])
	

	patch_name = u'ШОС-{:.1f}-{}-{}-{}-{}-{:.1f}м'.format(float(diametr), 
														  mod,
														  connectorLeft,
														  connectorRight,
														  cabel_type,
														  cabel_lenght)
	
	price = get_price_of_patch(cabel_lenght, 
							   connector_left_name, 
							   connector_right_name,
							   cabel_name,
							   cabel_type)
	return render_template('single_patch.html', name=patch_name, price=price)


