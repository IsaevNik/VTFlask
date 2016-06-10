# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
import os
import codecs
from collections import OrderedDict
from peewee import DoesNotExist

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
			img_path = os.path.join(base_dir,'app', 'static', 'shop', 'foto', str(line.foto) + '.jpg')
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
			img_path = os.path.join(base_dir,'app', 'static', 'shop', 'foto', str(line.foto) + '.jpg')
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

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/level1')
def level1():
	level = get_level('Сварочные аппараты ВОЛС')
	return render_template('level_base.html', level=level)

@app.route('/level2')
def level2():
	level = get_level('Измерительные приборы')
	return render_template('level_base.html', level=level)

@app.route('/level3')
def level3():
	level = get_level('Техническое обслуживание и ремонт приборов')
	return render_template('level_base.html', level=level)

@app.route('/level4')
def level4():
	level = get_level('Кроссовое оборудование')
	return render_template('level_base.html', level=level)

@app.route('/level5')
def level5():
	level = get_level('Пигтейлы оптические')
	return render_template('level_base.html', level=level)

@app.route('/level6')
def level6():
	level = get_level('Розетки оптические')
	return render_template('level_base.html', level=level)

@app.route('/level7')
def level7():
	level = get_level('Патч-корды')
	return render_template('level_base.html', level=level)

@app.route('/level8')
def level8():
	level = get_level('Материалы для производства патч-кордов')
	return render_template('level_base.html', level=level)

@app.route('/level9')
def level9():
	level = get_level('Расходные материалы и инструмент')
	return render_template('level_base.html', level=level)

@app.route('/level10')
def level10():
	level = get_level('Аттенюаторы')
	return render_template('level_base.html', level=level)

@app.route('/level11')
def level11():
	level = get_level('Разветвители оптические')
	return render_template('level_base.html', level=level)

@app.route('/level12')
def level12():
	level = get_level('Кабели связи')
	return render_template('level_base.html', level=level)

@app.route('/level13')
def level13():
	level = get_level('Кабельная арматура')
	return render_template('level_base.html', level=level)

@app.route('/level14')
def level14():
	level = get_level('Муфты для кабелей связи')
	return render_template('level_base.html', level=level)

@app.route('/level15')
def level15():
	level = get_level('Материалы для распределительных сетей')
	return render_template('level_base.html', level=level)

@app.route('/level16')
def level16():
	level = get_level('Линейные сооружения связи')
	return render_template('level_base.html', level=level)

@app.route('/level17')
def level17():
	level = get_level('Шкафы и стойки')
	return render_template('level_base.html', level=level)

@app.route('/level18')
def level18():
	level = get_level('Оборудование связи')
	return render_template('level_base.html', level=level)

@app.route('/search', methods=['POST'])
def search():
	userRequest = request.get_json()
	level = search_on_db(userRequest['text'])
	return render_template('level_base.html', level=level)