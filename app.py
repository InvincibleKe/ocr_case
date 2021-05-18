
from flask import Flask, request, Response, jsonify, make_response
from flask_restful import Resource, Api, reqparse, abort, Headers
from flask_cors import CORS
import os
import json
import recognition_zkktzs
import recognition_dsfzhxxd
compress = os.environ['COMPRESS']
app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
class Product(Resource):
    def get(self):
        return {'msg': 'Please use POST method'}
    def post(self):
        compress = os.environ['COMPRESS']
        parser = reqparse.RequestParser()
        parser.add_argument('model', type=str, required=True)
        parser.add_argument('image', type=str, required=True)
        args = parser.parse_args()
        model = args['model']
        #image_file = request.files['image']
        img_b64 = args['image']
        result = {}
        message = ''
        error = ''
        # 可以在此处增加模型
        if model == 'ZKKTZS':
            result = recognition_zkktzs.imgFile_recognition(img_b64, compress)
            code = 0
        elif model == 'DSFZHXXD':
            result = recognition_dsfzhxxd.imgFile_recognition(img_b64, compress)
            code = 0
        else:
            message = 'The required model does not exist'
            code = 1
        data = {'result': result, 'code': code, 'message': message, 'error': error}
        # data_return = json.dumps(data, ensure_ascii=False)
        res = make_response(jsonify(data))
        res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Method'] = '*'
        res.headers['Access-Control-Allow-Headers'] = '*'
        return res
api.add_resource(Product, '/api/v1/AI_detect')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,threaded=True, debug=True)