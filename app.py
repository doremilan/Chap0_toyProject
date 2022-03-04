from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://<id>:<pw>@cluster0.xkvvx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index_sub')
def index_sub():
    return render_template('index_sub.html')

@app.route("/mnt_info", methods=["POST"])
def movie_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST 연결 완료!'})

#  지역별 필터 기능
@app.route("/mnt_select", methods=["POST"])
def mnt_select():
    area_receive = request.form["area_give"]
    search_list = list(db.mnt_info.find({"mnt_area": area_receive}, {'_id': False}))
    return jsonify({'area_list':search_list})

@app.route("/mnt_info", methods=["GET"])
def mnt_get():
    all_mnt = list(db.mnt_info.find({},{'_id':False}))
    return jsonify({'mnt': all_mnt})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
