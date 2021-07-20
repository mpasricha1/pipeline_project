import sqlalchemy as db
from logger import Logger
import pandas as pd

class Database:
	def __init__(self):
		self.engine = ''
		self.logger = Logger()

	def establish_connection(self):
		try:
			self.engine = db.create_engine('postgres+psycopg2://postgres:postgres@localhost/pipeline_db_dev')
			self.logger.log_info("Connection Established")
		except Exception as e: 
			self.logger.log_error(e)

	def insert_to_temp_table(self, table_name, data):
		try:
			data.to_sql(table_name, self.engine, if_exists='replace', chunksize=None)
		except Exception as e:
			self.logger.log_error(e)
		finally:
			self.logger.log_rowcount(len(data))