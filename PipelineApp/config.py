import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = True
	CSRF_ENABLED = True
	SECRET_KEY = os.environ.get('SECRET_KEY')
	#SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost/pipeline_db_dev"
	SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:tableBlackCream177@threepm-dev1.chj3uciqytlo.us-east-1.rds.amazonaws.com:5432/threepm-dev1"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
