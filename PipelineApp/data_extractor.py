from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import requests
import io
import time

class extractor:
	def pull_loc_data(self):
		# Algonquin
		# url = "https://linkwc.spectraenergy.com/Pointdata/AgtAllPoints.csv"
		# # ETENN
		# url = "https://linkwc.spectraenergy.com/Pointdata/EtAllPoints.csv"
		# # Maritime
		# url = "https://linkwc.spectraenergy.com/Pointdata/MnusAllPoints.csv"
		# # Nexus
		# url = "https://linkwc.spectraenergy.com/Pointdata/NXUSAllPoints.csv"
		# # Ozark
		# url = "https://linkwc.spectraenergy.com/Pointdata/OgtAllPoints.csv"
		# # SESH
		# url = "https://linkwc.spectraenergy.com/Pointdata/SeshAllPoints.csv"
		# # Sabal
		# url = "https://linkwc.spectraenergy.com/Pointdata/STTAllPoints.csv"
		# # TETCO
		# url = "https://linkwc.spectraenergy.com/Pointdata/TeAllPoints.csv"

		request = requests.get(url)
		df = pd.DataFrame(pd.read_csv(io.StringIO(request.content.decode("utf-8"))))
		print(df)
	 
		return df

	def pull_flow_data(self):
		# Algonquin
		url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=AG&Type=OA"
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

		target = {
			"ctl00$MainContent$ctl01$oaDefault$hlDown$LinkButton1"
		}
		# target = {"ctl00$MainContent$ctl01$oaDefault$ucDate$rdpDate"}

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

			view_state = soup.find("input", {"id": "__VIEWSTATE"})["value"]
			validation = soup.find("input", {"id": "__EVENTVALIDATION"})["value"]
			
			request = s.post(url, data={
				"__EVENTTarget": target,
				"__VIEWSTATE": view_state, 
				"__EVENTVALIDATION": validation, 
				"ddlSelector" : "LATE_2020-12-20_0900"

				})
			soup = BeautifulSoup(request.content, "html.parser")
			df = pd.DataFrame(pd.read_csv(io.StringIO(request.content.decode("utf-8"))))

		print(df)
		return df

	def scraper(self): 
		

		url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=ET&Type=OA"

	

		html = browser.html
		soup = bs(html,"html.parser")

		browser.links.find_by_text("Downloadable Format")

		browser.quit()