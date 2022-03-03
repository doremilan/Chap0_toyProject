from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://<id>:<pw>@cluster0.xkvvx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index_sub.html')

@app.route("/hiking", methods=["POST"])
def hiking_post():
    name_receive = request.form["name_give"]
    star_receive = request.form["star_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'star': star_receive
    }
    db.hiking.insert_one(doc)
    return jsonify({'msg':'등록 완료'})

@app.route("/hiking", methods=["GET"])
def hiking_get():
    cmt_list = list(db.hiking.find({}, {'_id': False}))
    return jsonify({'comment':cmt_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)