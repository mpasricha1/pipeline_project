from data_extractor import Extractor
from database import Database
from logger import Logger
from datetime import datetime

url = 'https://tgcmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=TGC&gasDay=07%2F19%2F2021&cycleDesc=Intraday%202&pointCd=&name='

logger = Logger()
logger.create_logs("test")

scraper = Extractor(datetime.now())
db = Database()
db.establish_connection()

data = scraper.pull_loc_data(url)

db.insert_to_temp_table('temp_flow_data', data)

