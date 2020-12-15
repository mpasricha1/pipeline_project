from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import io

class extractor:
	def __init__(self):
		self.data = ""

	def pull_data(self):
		# url = "https://linkwc.spectraenergy.com/Pointdata/AgtAllPoints.csv"
		# url = "https://linkwc.spectraenergy.com/Pointdata/EtAllPoints.csv"
		url = "https://peplmessenger.energytransfer.com/ipost/locations/index?f=csv&extension=csv&asset=PEPL&gasDay=2"

		request = requests.get(url, allow_redirects=True)
		url_content = request.content

		df = pd.DataFrame(pd.read_csv(io.StringIO(url_content.decode("utf-8"))))

		print(df)

		return df

	def scraper(self): 
		executable_path = {'executable_path': 'chromedriver.exe'}
		browser = Browser('chrome', **executable_path, headless=False)

		url = "https://rtba.spectraenergy.com/InformationalPosting/Default.aspx?bu=ET&Type=OA"

		browser.visit(url)

		html = browser.html
		soup = bs(html,"html.parser")

		browser.links.find_by_text("Downloadable Format")
		

		browser.quit()