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


	def test_for_git():
		return