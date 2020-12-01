from app import db 

class pipeline_location(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pipeline_id = db.Column(db.Integer)
	loc_id = db.Column(db.String())
	name = db.Column(db.String())
	state = db.Column(db.String())
	county = db.Column(db.String())
	zone = db.Column(db.String())
	flow_direction = db.Column(db.Integer)
	loc_type = db.Column(db.String())
	created_at = db.Column(db.DateTime)
	updated_at = db.Column(db.DateTime)
	has_missing_details = db.Column(db.Boolean)

	def __repr__(self):
		return '<pipeline_location {}>'.format(self.username)

