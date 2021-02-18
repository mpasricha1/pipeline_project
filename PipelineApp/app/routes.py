from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
from flask_migrate import Migrate
from data_extractor import extractor
from db_util import db_util
from app import app 


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
	db = db_util()
	# extract = extractor()
	# url_list = db.generate_flow_url_list("Energy Transfer")

	# for url in url_list:
	# 	if url["url"] != '':
	# 		data = extract.pull_energy_transfer_flow_data(url)
	# 		# db.insert_new_flow_data(data)
	# 	else:
	# 		pass

	pipelines = db.generate_pipeline_names()
	print(pipelines)
	firstPipeline = pipelines[0][0]
	locs = db.generate_locs_by_pipeline(firstPipeline)

	if request.method == "POST":
		returnVal = request.form.get("val")
		print(returnVal)
	

	return render_template("index.html", pipelines=pipelines, locs=locs)