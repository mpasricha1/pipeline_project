from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.models import pipeline_location, flow_readings
from app import db


class db_util: 
	def insert_new_loc_data(self,df):
		for index, row in df.iterrows():
			exists = pipeline_location.query.filter_by(loc_id=str(row["Loc"])).first() is not None
			if exists == True:
				print("Loc already in database")
				pass
			else:
				pl = pipeline_location(pipeline_id=1,loc_id=row["Loc"], name=row["Loc Name"], state=row["Loc St Abbrev"], county=row["Loc Cnty"],
										zone=row["Loc Zone"], flow_direction=row["Dir Flo"], loc_type=row["Loc Type Ind"], 
										created_at=datetime.now(), updated_at=datetime.now(), has_missing_details=None)
				db.session.add(pl)
				db.session.commit()
				print("Loc not found")


	def insert_new_flow_data(self,df):
		for index, row in df.iterrows():
			try:
				pipe_loc = pipeline_location.query.filter_by(loc_id = str(row["Loc"])).first()
				fr = flow_readings(pipeline_location_id=pipe_loc.id, loc_id=row["Loc"], flow_date=row["Eff_Gas_Day"], 
									oc=int(row["Operating_Capacity"].replace(",","")), tsq=int(row["Total_Scheduled_Quantity"].replace(",","")), 
									flow_dir=row["Flow_Ind_Desc"], created_at=datetime.now(), updated_at=datetime.now())
				db.session.add(fr)
				db.session.commit()
			except:
				print("Loc Not Found")
		
