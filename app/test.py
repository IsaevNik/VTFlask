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

get_table('PassivnyeKomponentyVols')