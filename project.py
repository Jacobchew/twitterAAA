import os,re,math
from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template(index.html)


@app.route('/biscuit')
def 


if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host = '0.0.0.0', port = port)
