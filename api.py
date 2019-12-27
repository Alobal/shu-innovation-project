from flask import Flask, request, jsonify
from flask_cors import CORS
import beike
import lianjia
import transform


app = Flask(__name__)

# 解决跨域
CORS(app, supports_credentials=True)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/house', methods=['GET'])
def bei():
    platform = request.args['platform']
    city = request.args['city']
    typeh = request.args['type']
    page = int(request.args['page'])
    try:
        if platform == 'beike':
            return beike.run(city, typeh, page)
        if platform == 'lianjia':
            return lianjia.run(city, typeh, page)
    except Exception as e:
        return jsonify({"code": 404, "message": str(e)})


    
app.run(host='0.0.0.0')