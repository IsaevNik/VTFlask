from flask import Flask, render_template, jsonify

app = Flask(__name__)


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

@app.route('/contacts')
def contacts():
	return render_template('contacts.html')

if __name__ == '__main__':
	app.run(debug=True)