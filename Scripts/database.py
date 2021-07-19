import sqlalchemy as db

class Database():
	engine = db.create_engine('postgres+psycopg2://postgres:postgres@localhost/pipeline_db_dev') 

	def __init__(self):
		try:
			self.connection = self.engine.connect()
			print('Connected to Database')
		except Exception as e: 
			print(e)

