from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from datetime import datetime
from app.models import pipeline_location, flow_readings, pipelines
from app import db


class db_util: 
	def generate_loc_url_list(self,provider):
	 	loc_list = pipelines.query.filter_by(provider=provider).all()

	 	url_list = []
	 	for loc in loc_list:
	 		url_list.append(loc.loc_file_url)

	 	return url_list

	def insert_new_loc_data(self,df):
		for index, row in df.iterrows():
			exists = pipeline_location.query.filter_by(loc_id=str(row["Loc"])).first() is not None
			if exists == True:
				print("Loc already in database")
				pass
			else:
				pipeline = pipelines.query.filter_by(tsp=row["TSP"]).first()
				if row["Dir Flo"].lower() == 'b':
					print("Found Bi Directional")
					dirFlow = ["D", "R"]
					for x in dirFlow:
						pl = pipeline_location(pipeline_id=pipeline.id,loc_id=row["Loc"], name=row["Loc Name"], state=row["Loc St Abbrev"], county=row["Loc Cnty"],
												zone=row["Loc Zone"], flow_direction=x, loc_type=row["Loc Type Ind"], 
												created_at=datetime.now(), updated_at=datetime.now(), has_missing_details=None)
						db.session.add(pl)
						db.session.commit()
				else:
					pl = pipeline_location(pipeline_id=pipeline.id,loc_id=row["Loc"], name=row["Loc Name"], state=row["Loc St Abbrev"], county=row["Loc Cnty"],
												zone=row["Loc Zone"], flow_direction=row["Dir Flo"], loc_type=row["Loc Type Ind"], 
												created_at=datetime.now(), updated_at=datetime.now(), has_missing_details=None)
					db.session.add(pl)
					db.session.commit()

				print("Loc not found")

#loc, flow direction, pipeline name 
	def insert_new_flow_data(self,df):
		exists = flow_readings.query.filter_by(cycle_desc=df["Cycle_Desc"].iloc[0]).first() is not None
		if exists == True:
			return
		else:
			for index, row in df.iterrows():
				if row["Flow_Ind_Desc"].lower() == "delivery" or row["Flow_Ind_Desc"].lower() == "storage injection":
					flow_dir = "D"
				else:
					flow_dir = "R" 
				exists = pipeline_location.query.filter_by(loc_id=str(row["Loc"]), flow_direction=flow_dir).first() is not None
				if exists == True:
					print(flow_dir)
					loc = pipeline_location.query.filter_by(loc_id=str(row["Loc"]), flow_direction=flow_dir).first()
					fr = flow_readings(pipeline_location_id=loc.id, loc_id=row["Loc"], flow_date=row["Eff_Gas_Day"], 
											oc=int(row["Operating_Capacity"].replace(",","")), tsq=int(row["Total_Scheduled_Quantity"].replace(",","")), 
											flow_dir=row["Flow_Ind_Desc"], created_at=datetime.now(), updated_at=datetime.now(), cycle_desc=row["Cycle_Desc"])
					db.session.add(fr)
					db.session.commit()
				else:
					print("Inserting New Loc")
					pipeline = pipelines.query.filter_by(tsp=row["TSP"]).first()
					pl = pipeline_location(pipeline_id=pipeline.id,loc_id=row["Loc"], name=row["Loc_Name"], state=None, county=None,
													zone=row["Loc_Zn"], flow_direction=flow_dir, loc_type=None, 
													created_at=datetime.now(), updated_at=datetime.now(), has_missing_details=True)
					db.session.add(pl)
					db.session.commit()
					
					loc = pipeline_location.query.filter_by(loc_id=str(row["Loc"])).first()
					fr = flow_readings(pipeline_location_id=loc.id, loc_id=row["Loc"], flow_date=row["Eff_Gas_Day"], 
										oc=int(row["Operating_Capacity"].replace(",","")), tsq=int(row["Total_Scheduled_Quantity"].replace(",","")), 
										flow_dir=row["Flow_Ind_Desc"], created_at=datetime.now(), updated_at=datetime.now(), cycle_desc=row["Cycle_Desc"])
					db.session.add(fr)
					db.session.commit()
			
