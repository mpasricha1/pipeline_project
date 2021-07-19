import logging
from datetime import datetime

class Logger():
	def create_logs(self,name):
		logging.basicConfig(filename=f'{name}_Log_{datetime.now().strftime("%Y-%m-%d-%H:%M%S")}.txt', level=logging.DEBUG)

	