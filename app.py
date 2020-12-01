from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/agantio_db"
app.config['MONGO_DBNAME'] = "agantio_db"

mongo = PyMongo(app)

@app.route("api/timecapsules", methods = ["GET"])
def get_capsules():
	outputs = []
	for q in mongo.db.timecapsules.find():
		outputs.append({'id' : q['id'], 'name' : q['name'], 'location' : q['location'], 'raduis' : q['radius'], 'title' : q['title'], 'content' : q['content'], 'icon' : q['icon'], 'point' : q['point']})
	return jsonify({'result' : outputs})

@app.route("api/questions", methods = ["GET"])
def get_questions():
	outputs = []
	for q in mongo.db.questions.find():
		outputs.append({'firstquestions': q['firstquestions'], 'lastquestions': q['lastquestions']})
	return jsonify({'result' : outputs})


@app.route("api/ranks", methods = ["GET"])
def get_ranks():
	outputs = []
	for r in mongo.db.ranks.find():
		outputs.append({'man': r['man'], 'woman': r['woman']})
	return jsonify({'result' : outputs})


if __name__ == "__main__":
    app.run(debug=True)