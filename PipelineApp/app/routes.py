from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
from sqlalchemy.ext.automap import automap_base 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine, and_, func
from sqlalchemy.orm import Session
from app import app 

@app.route('/')
@app.route('/index')
def index():
	return render_template("base.html")