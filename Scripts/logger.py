import logging
from datetime import datetime

class Logger():
	def create_logs(self,name):
		logging.basicConfig(filename=f'{name}_Log_{datetime.now().strftime("%Y-%m-%d-%H:%M%S")}.txt', level=logging.DEBUG)

	def log_info(self, message):
		logging.info(f'{datetime.now().strftime("%Y-%m-%d-%H:%M%S")} :: {message}')

	def log_error(self, message):
		logging.error(f'{datetime.now().strftime("%Y-%m-%d-%H:%M%S")} :: {message}')

	def log_rowcount(self, count):
		logging.info(f'{datetime.now().strftime("%Y-%m-%d-%H:%M%S")} :: {count} rows inserted to temp table')