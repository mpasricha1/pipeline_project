from data_extractor import extractor
import time
from datetime import datetime

def get_current_time():
	now = datetime.now()
	current_date = now.strftime('%Y-%m-%d')
	current_time = now.strftime('%H:%M:%S')

	return current_time, current_date

def create_extractor():
	

def get_energy_transfer_data():
	file_list = ['Timely', 'Evening', 'Final', 'Intraday%201', 'Intraday%202', 'Intraday%203']
	curr_time, curr_date = get_current_time()
	extract = extractor(curr_date)

	while extract.scrape_complete == False:
		curr_time, curr_date = get_current_time()

		if curr_time >= "18:00:00" or curr_time < "22:00:00":
			file_to_search = file_list[0]
		else if curr_time >= "22:00:00"
		url_list = db.generate_flow_url_list("Energy Transfer")

		for url in url_list:
			if url["url"] != '':
				data = extract.pull_energy_transfer_flow_data(url)
				db.insert_new_flow_data(data)
			else:
				pass
		# time

get_energy_transfer_data()