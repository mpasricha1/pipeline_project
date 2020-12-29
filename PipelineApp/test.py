from data_extractor import extractor
# from db_util import db_util


extract = extractor()
data = extract.pull_data()
db = db_util() 
db.insert_new_flow_data(data)
