# from data_extractor import extractor
# from db_util import db_util

from datetime import datetime

def get_current_time():
	now = datetime.now()
	current_date = now.strftime('%Y-%m-%d')
	current_time = now.strftime('%H:%M:%S')

	return current_time, current_date


def get_energy_transfer_data():
	file_list = ['Timely', 'Evening', 'Final', 'Intraday%201', 'Intraday%202', 'Intraday%203']
	time, date = get_current_time()
	if time >
	print(time)
	db = db_util()
	extract = extractor()
	url_list = db.generate_flow_url_list("Energy Transfer")

	for url in url_list:
		if url["url"] != '':
			data = extract.pull_energy_transfer_flow_data(url)
			db.insert_new_flow_data(data)
		else:
			pass

current_time, current_date = get_current_time()
print(current_time)
print(current_date)