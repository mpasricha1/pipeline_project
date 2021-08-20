import sqlalchemy as db
from logger import Logger
import pandas as pd
import psycopg2

class Database:
	def __init__(self):
		self.engine = ''
		self.logger = Logger()

	def establish_connection(self):
		try:
			self.engine = db.create_engine('postgresql+psycopg2://postgres:post259mzj!@pipeline-db-dev.coj14rnbchxk.us-east-2.rds.amazonaws.com:5432/pipeline_db_dev')
			self.logger.log_info("Connection Established")
		except Exception as e: 
			self.logger.log_error(e)

	def truncate_table(self,table): 
		try:
			with self.engine.begin() as conn:
				conn.execute(f'Truncate table {table}')
		except Exception as e: 
			self.logger.log_error(e)
			print(e)

	def exec_stp(self, stp_name):
		try:
			with self.engine.begin() as conn: 
				conn.execute(f'Call public.{stp_name}')
		except Exception as e: 
			self.logger.log_error(e)
			print(e)

	def insert_to_temp_table(self, table_name, data):
		try:
			data.to_sql(table_name, self.engine, if_exists='append', chunksize=None)
		except Exception as e:
			self.logger.log_error(e)
		finally:
			self.logger.log_rowcount(len(data))
