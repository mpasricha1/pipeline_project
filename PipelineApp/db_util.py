from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.models import pipeline_location, flow_readings
from app import db


class db_util: 
	def insert_new_location(self,df):
		for index, row in df.iterrows():
			pl = pipeline_location(pipeline_id=1,loc_id=row["Loc"], name=row["Loc Name"], state=row["Loc St Abbrev"], county=row["Loc Cnty"],
									zone=row["Loc Zone"], flow_direction=row["Dir Flo"], loc_type=row["Loc Type Ind"], 
									created_at=datetime.now(), updated_at=datetime.now(), has_missing_details=None)
			db.session.add(pl)
			db.session.commit()

			# pl_id = pipeline_location.query.order_by(pipeline_location.id.desc()).first()
			# fr = flow_readings(pipeline_location_id=pl_id, flow_date=datetime.now(), oc=)
			# print(pl_id.id)

