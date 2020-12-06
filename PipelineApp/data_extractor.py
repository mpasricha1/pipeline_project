import pandas as pd
import requests
import io
from datetime import datetime
from app.models import pipeline_location
from app import db



class extractor:
	def __init__(self):
		self.data = ""

	def pull_data(self):
		# url = "https://linkwc.spectraenergy.com/Pointdata/AgtAllPoints.csv"
		url = "https://linkwc.spectraenergy.com/Pointdata/EtAllPoints.csv"

		request = requests.get(url, allow_redirects=True)
		url_content = request.content

		df = pd.DataFrame(pd.read_csv(io.StringIO(url_content.decode("utf-8"))))

		for index, row in df.iterrows():
			pl = pipeline_location(pipeline_id=1,loc_id=row["Loc"], name=row["Loc Name"], state=row["Loc St Abbrev"], county=row["Loc Cnty"],
									zone=row["Loc Zone"], flow_direction=row["Dir Flo"], loc_type=row["Loc Type Ind"], 
									created_at=datetime.now(), updated_at=datetime.now(), has_missing_details=None)
			db.session.add(pl)
			db.session.commit()
		
