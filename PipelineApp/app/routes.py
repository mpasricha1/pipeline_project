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
	db = db_util()
	data = extract.pull_data()
	db.insert_new_location(data)
	
	return render_template("index.html")