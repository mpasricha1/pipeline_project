from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app 

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")