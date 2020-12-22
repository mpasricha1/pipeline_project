from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import requests
import io
import time

class extractor:
	def __init__(self):
		self.data = ""

	def pull_data(self):
		# url = "https://linkwc.spectraenergy.com/Pointdata/AgtAllPoints.csv"
		# url = "https://linkwc.spectraenergy.com/Pointdata/EtAllPoints.csv"
		#url = "https://peplmessenger.energytransfer.com/ipost/locations/index?f=csv&extension=csv&asset=PEPL&gasDay=2"
		url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=ET&Type=OA"
		target = {
			"ctl00$MainContent$ctl01$oaDefault$hlDown$LinkButton1"
		}
		# target = {"ctl00$MainContent$ctl01$oaDefault$ucDate$rdpDate"}

		# executable_path = {'executable_path': 'chromedriver.exe'}
		# browser = Browser('chrome', **executable_path, headless=False)

		browser = webdriver.Chrome(executable_path="chromedriver.exe")
		browser.get(url)

		date_field = browser.find_element_by_id("ctl00_MainContent_ctl01_oaDefault_ucDate_rdpDate_dateInput_text")
		date_field.send_keys(Keys.BACKSPACE*10)
		date_field.send_keys('12/14/2020')
		date_field.click()
		time.sleep(10)
		print(date_field.get_attribute("value"))

		browser.refresh()
		drop_down = browser.find_element_by_id("ddlSelector")
		print(drop_down.get_attribute("value"))

		# html = browser.page_source
		# soup = BeautifulSoup(html, 'html.parser')
		# print(soup)

		# with requests.session() as s:
		# 	s.headers["user-agent"] = "Mozilla/5.0"

		# 	request = s.get(url, allow_redirects=True)
		# 	soup = BeautifulSoup(request.content, "html.parser")

		# 	view_state = soup.find("input", {"id": "__VIEWSTATE"})["value"]
		# 	validation = soup.find("input", {"id": "__EVENTVALIDATION"})["value"]
			
		# 	request = s.post(url, data={
		# 		"__EVENTTarget": target,
		# 		"__VIEWSTATE": view_state, 
		# 		"__EVENTVALIDATION": validation, 
		# 		"ddlSelector" : "LATE_2020-12-20_0900"

		# 		})
		# 	soup = BeautifulSoup(request.content, "html.parser")
		# 	print(soup)
			# df = pd.DataFrame(pd.read_csv(io.StringIO(request.content.decode("utf-8"))))
			# print(df)

		# print(df)

		# return df

	def scraper(self): 
		

		url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=ET&Type=OA"

	

		html = browser.html
		soup = bs(html,"html.parser")

		browser.links.find_by_text("Downloadable Format")

		browser.quit()