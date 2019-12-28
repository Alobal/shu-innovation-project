from flask import Flask, request, jsonify
from flask_cors import CORS
import beike
import lianjia
import ziru
import zhaopin
import job51
import lagou


app = Flask(__name__)

# 解决跨域
CORS(app, supports_credentials=True)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/house', methods=['GET'])
def house():
    platform = request.args['platform']
    city = request.args['city']
    typeh = request.args['type']
    page = int(request.args['page'])
    try:
        if platform == 'beike':
            return beike.run(city, typeh, page)
        if platform == 'lianjia':
            return lianjia.run(city, typeh, page)
        if platform == 'ziru':
            return ziru.run(city, page)
    except Exception as e:
        return jsonify({"code": 404, "message": str(e)})


@app.route('/job', methods=['GET'])
def job():
    platform = request.args['platform']
    city = request.args['city']
    job = request.args['job']
    page = int(request.args['page'])
    try:
        if platform == 'zhaopin':
            return zhaopin.run(city, job, page)
        if platform == '51':
            return job51.run(city, job, page)
        if platform == 'lagou':
            return lagou.run(city, job, page)
    except Exception as e:
        return jsonify({"code": 404, "message": str(e)})

    
app.run(host='0.0.0.0', port=8080)