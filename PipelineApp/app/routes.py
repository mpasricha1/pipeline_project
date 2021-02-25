from flask import render_template, request, redirect, session, url_for
from flask.json import jsonify
from redis import Redis 
import rq 
from flask_migrate import Migrate
from data_extractor import extractor
from db_util import db_util
from app import tasks
from app import app 


db = db_util()

tasks.get_energy_transfer_data();
# queue = rq.Queue('pipeline-tasks', connection=Redis.from_url('redis://'))
# job = queue.enqueue("app.tasks.get_energy_transfer_data", 20)


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
	

	pipelines = db.generate_pipeline_names()
	# print(pipelines)
	firstPipeline = pipelines[0][0]
	locs = db.generate_locs_by_pipeline(firstPipeline)

	if request.method == "POST":
		returnVal = request.form.get("val")
		print(returnVal)
	

	return render_template("index.html", pipelines=pipelines, locs=locs)