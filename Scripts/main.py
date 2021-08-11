from data_extractor import Extractor
from database import Database
from logger import Logger
from datetime import datetime
import sys

args = sys.argv[1:]
print(args[0])

url = 'https://peplmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=PEPL&gasDay=08%2F10%2F2021&cycleDesc=Timely&pointCd=&name='
url2 = 'https://peplmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=PEPL&gasDay=08%2F10%2F2021&cycleDesc=Evening&pointCd=&name='
url3 = 'https://peplmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=PEPL&gasDay=08%2F11%2F2021&cycleDesc=Intraday%201&pointCd=&name='
url4 = 'https://peplmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=PEPL&gasDay=08%2F11%2F2021&cycleDesc=Intraday%202&pointCd=&name='
url5 = 'https://peplmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=PEPL&gasDay=08%2F11%2F2021&cycleDesc=Intraday%203&pointCd=&name='
url6 = 'https://peplmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=PEPL&gasDay=08%2F010%2F2021&cycleDesc=Final&pointCd=&name='

logger = Logger()
logger.create_logs("test")

scraper = Extractor(datetime.now())
db = Database()
db.establish_connection()

if args[0].lower() == 'timely':
	data = scraper.pull_loc_data(url)
	db.insert_to_temp_table('temp_flow_timely', data)
elif args[0].lower() == 'evening':
	data = scraper.pull_loc_data(url2)
	db.insert_to_temp_table('temp_flow_evening', data)
elif args[0].lower() == 'id1':
	data = scraper.pull_loc_data(url3)
	db.insert_to_temp_table('temp_flow_id1', data)
elif args[0].lower() == 'id2':
	data = scraper.pull_loc_data(url4)
	db.insert_to_temp_table('temp_flow_id2', data)
elif args[0].lower() == 'id3':
	data = scraper.pull_loc_data(url5)
	db.insert_to_temp_table('temp_flow_id3', data)
elif args[0].lower() == 'final':
	data = scraper.pull_loc_data(url6)
	db.insert_to_temp_table('temp_flow_final', data)




# data = scraper.pull_loc_data(url)
# db.insert_to_temp_table('temp_flow_data', data)

