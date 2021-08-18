
from data_extractor import Extractor
from database import Database
from logger import Logger
from datetime import datetime
import sys

args = sys.argv[1:]
print(args[0])

urls = [
		'https://peplmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=PEPL&gasDay={}&cycleDesc={}&pointCd=&name=',
		'https://rovermessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=ROVER&gasDay={}&cycleDesc={}&pointCd=&name=', 
		'https://sermessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=SER&gasDay={}&cycleDesc={}&pointCd=&name=',
		#'https://fgttransfer.energytransfer.com/ipost/capacity/operationally-available?f=csv&extension=csv&asset=FGT&gasDay={}&cycle={}&searchType=NOM&searchString=&locType=ALL&locZone=ALL',
		'https://tgcmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=TGC&gasDay={}&cycleDesc={}&pointCd=&name='
	   ]


logger = Logger()
logger.create_logs("test")

scraper = Extractor(datetime.now())
db = Database()
db.establish_connection()

for url in urls: 
	data = scraper.pull_energy_transfer_flow_data(url, args[0])
	db.insert_to_temp_table(f'temp_flow_{args[0]}', data)



