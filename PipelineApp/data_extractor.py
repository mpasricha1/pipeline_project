from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import requests
import io
import time

# https://peplmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=PEPL&gasDay=01%2F14%2F2021&
# https://peplmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=PEPL&gasDay=01%2F15%2F2021&cycleDesc=Intraday%202&pointCd=&name=
# https://peplmessenger.energytransfer.com/ipost/capacity/operationally-available-by-location?f=csv&extension=csv&asset=PEPL&gasDay=01%2F16%2F2021&cycleDesc=Timely&pointCd=&name=
class extractor:

	def generate_date_for_url(self, cycle):
		if cycle == 'Final' or cycle == 'Timely' or  cycle =='Evening':
			date = datetime.today() - timedelta(days=1)
		else:
			date = datetime.today()

		url_date = f"{date.month}%2F{date.day}%2F{date.year}"

		return url_date
		
	def generate_cycle_count(self,tsp, cycle):
		return f"{cycle}-{(datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')}-{tsp}"

	def pull_loc_data(self, url):
		request = requests.get(final_url)
		df = pd.DataFrame(pd.read_csv(io.StringIO(request.content.decode("utf-8"))))

		print(df)
		return df		

	def pull_energy_transfer_flow_data(self,url):
		file_list = ['Timely', 'Evening', 'Final', 'Intraday%201', 'Intraday%202', 'Intraday%203']
		master_df = pd.DataFrame()

		for file in file_list:

			final_url = url["url"].format(self.generate_date_for_url(file),file)
			print(final_url)

			request = requests.get(final_url)
			df = pd.DataFrame(pd.read_csv(io.StringIO(request.content.decode("utf-8"))))

			df["Cycle_Desc"] = self.generate_cycle_count(url["tsp"],file)
			df["Eff_Gas_Day"] = datetime.today() - timedelta(days=1)
			df["TSP"] = url["tsp"]
			df.rename(columns={"Flow Ind": "Flow_Ind_Desc", "OPC": "Operating_Capacity", 
							   "TSQ": "Total_Scheduled_Quantity", "Loc Zn": "Loc_Zn", "Loc Name": "Loc_Name"}, inplace=True)

			if url["tsp"] == 6924518:
				df["Total_Scheduled_Quantity"] = df["TSQ (Rec)"] + df["TSQ (Del)"]

			print(df)
			master_df = master_df.append(df)
			
		# print(master_df)
		master_df.to_csv("final.csv")
		return master_df

	def pull_flow_data(self):
		# Specter
		# Algonquin
		# url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=AG&Type=OA"
		# # ETENN
		# url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=ET&Type=OA"
		# # Maritime
		# url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=TE&Type=OA"
		# # Nexus
		# url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=NXUS&Type=OA"
		# # Ozark
		# url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=OGT&Type=OA"
		# # SESH
		# url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=SESH&Type=OA"
		# # Sabal
		# url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=STT&Type=OA"
		# TETCO
		# url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=TE&Type=OA"

		#Kinder Morgan
		#Elba
		# url = "https://pipeline2.kindermorgan.com/Capacity/OpAvailSegment.aspx?code=EEC"

		#Boardwalk
		#Gulf 
		url = "https://infopost.bwpipelines.com/Frameset.aspx?url=%2FPosting%2Fdefault.aspx%3FMode%3DDisplay%26Id%3D11&tspid=1"


		# target = {
		# 	"ctl00$MainContent$ctl01$oaDefault$hlDown$LinkButton1"
		# }
		# target = {"ctl00$WebSplitter1$tmpl1$ContentPlaceHolder1$HeaderBTN1$btnDownload"}

		browser = webdriver.Chrome(executable_path="chromedriver.exe")
		browser.get(url)

		# date_field = browser.find_element_by_id("ctl00_MainContent_ctl01_oaDefault_ucDate_rdpDate_dateInput_text")
		# date_field.send_keys(Keys.BACKSPACE*10)
		# date_field.send_keys('12/14/2020')
		# date_field.click()
		# time.sleep(10)
		# print(date_field.get_attribute("value"))

		# browser.refresh()
		# drop_down = browser.find_element_by_id("ddlSelector")
		# print(drop_down.get_attribute("value"))

		html = browser.page_source
		soup = BeautifulSoup(html, 'html.parser')

		with requests.session() as s:
			s.headers["user-agent"] = "Mozilla/5.0"

			request = s.get(url, allow_redirects=True)
			soup = BeautifulSoup(request.content, "html.parser")

			target = soup.find("input", {"id": "__EVENTTarget"})["value"]
			print(target)
			view_state = soup.find("input", {"id": "__VIEWSTATE"})["value"]
			validation = soup.find("input", {"id": "__EVENTVALIDATION"})["value"]
			
			request = s.post(url, data={
				"__EVENTTarget": target,
				"__VIEWSTATE": view_state, 
				"__EVENTVALIDATION": validation

				})
			soup = BeautifulSoup(request.content, "html.parser")
			print(request.text)
			# df = pd.DataFrame(pd.read_csv(io.StringIO(request.content.decode("utf-8"))))

		# print(df)
		# return df

	def scraper(self): 
		

		url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=ET&Type=OA"

	

		html = browser.html
		soup = bs(html,"html.parser")

		browser.links.find_by_text("Downloadable Format")

		browser.quit()