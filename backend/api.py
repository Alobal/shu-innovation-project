from flask import Flask, request, jsonify
from flask_cors import CORS
import beike
import lianjia
import ziru
import job51
import lagou
import fang
import liepin
import suning
import jingdong
import zhaopinBaidu

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
        # 只有二手房
        if platform == 'ziru':
            return ziru.run(city, page)
        # 只有二手房和租房两种类型
        if platform=='fang':
            return fang.run(city,typeh,page)
    except Exception as e:
        return jsonify({"code": 404, "message": str(e)})


@app.route('/job', methods=['GET'])
def job():
    platform = request.args['platform']
    city = request.args['city']
    job = request.args['job']
    page = int(request.args['page'])
    try:
        if platform == '51':
            return job51.run(city, job, page)
        if platform == 'lagou':
            return lagou.run(city, job, page)
        if platform == 'liepin':
            return liepin.run(city, job, page)
        if platform == 'baidu':
            return zhaopinBaidu(city, job, page)
    except Exception as e:
        return jsonify({"code": 404, "message": str(e)})


@app.route('/goods', methods=['GET'])
def goods():
    platform = request.args['platform']
    keyword = request.args['keyword']
    page = int(request.args['page'])
    try:
        if platform == 'jingdong':
            return jingdong.run(keyword, page)
        if platform == 'suning':
            return suning.run(keyword, page)          
    except Exception as e:
        return jsonify({"code": 404, "message": str(e)})


if __name__ == '__main__':
    # 不加这个 部署的时候会报错 address alread in use
    app.run(host='0.0.0.0', port=8080)