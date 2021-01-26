from app import db 

class pipelines(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	tsp = db.Column(db.Integer)
	created_at = db.Column(db.DateTime)
	updated_at = db.Column(db.DateTime)
	provider = db.Column(db.String())
	code = db.Column(db.String())
	loc_file_url = db.Column(db.String())
	flow_file_url = db.Column(db.String())

	def __repr__(self):
		return '<pipelines {}>'.format(self.name)

class pipeline_location(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pipeline_id = db.Column(db.Integer, db.ForeignKey("pipelines.id"))
	loc_id = db.Column(db.String())
	name = db.Column(db.String())
	state = db.Column(db.String())
	county = db.Column(db.String())
	zone = db.Column(db.String())
	loc_type = db.Column(db.String())
	flow_direction = db.Column(db.String())
	created_at = db.Column(db.DateTime)
	updated_at = db.Column(db.DateTime)
	has_missing_details = db.Column(db.Boolean)

	def __repr__(self):
		return '<pipeline_location {}>'.format(self.name)

class flow_readings(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	pipeline_location_id = db.Column(db.Integer, db.ForeignKey("pipeline_location.id"))
	loc_id = db.Column(db.String())
	flow_date = db.Column(db.Date)
	oc = db.Column(db.Integer)
	tsq = db.Column(db.Integer)
	flow_dir = db.Column(db.String())
	created_at = db.Column(db.DateTime)
	updated_at = db.Column(db.DateTime)
	cycle_desc = db.Column(db.String())


	def __repr__(self):
		return '<flow_readings {}>'.format(self.id)
