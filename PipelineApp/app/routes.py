from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
from flask_migrate import Migrate
from data_extractor import extractor
from db_util import db_util
from app import app 


@app.route('/')
@app.route('/index')
def index():
	extract = extractor()
	data = extract.pull_flow_data()
	# db = db_util() 
	# db.insert_new_flow_data(data)

	return render_template("index.html")