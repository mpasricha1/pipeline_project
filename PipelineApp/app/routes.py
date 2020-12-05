from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from data_extractor import extractor
from app import app 


@app.route('/')
@app.route('/index')
def index():
	extract = extractor()
	extract.pull_data()
	return render_template("index.html")