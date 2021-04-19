'''
from flask import Flask, request, jsonify, make_response
import json
import recognition_zkktzs
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/api/v1/AI_detect', methods=['POST', 'GET', 'OPTIONS'])
def upload():
    if request.method == 'GET':
        {'msg': 'Please use POST method'}
    else:
        image_file = request.files['image']
        model = request.form['model']
        if image_file and allowed_file(image_file.filename):
            result = {}
            message = ''
            if model == 'ZKKTZS':
                result = recognition_zkktzs.imgFile_recognition(image_file)
                code = 1
            else:
                message = 'The required model does not exist'
                code = 0
            data = {'result': result, 'code': code, 'message': message}
            res = make_response(jsonify({'data': data}))
            res.headers['Access-Control-Allow-Origin'] = '*'
            res.headers['Access-Control-Allow-Method'] = '*'
            res.headers['Access-Control-Allow-Headers'] = '*'
            return res
        else:
            return 'The file format must be png, jpg, jpeg or gif.'
if __name__ == '__main__':
    app.run(debug=True)
'''
from flask import Flask, request, Response, jsonify, make_response
from flask_restful import Resource, Api, reqparse, abort, Headers
from flask_cors import CORS
import json
import recognition_zkktzs
app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
class Product(Resource):
    def get(self):
        return {'msg': 'Please use POST method'}
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('model', type=str, required=True)
        parser.add_argument('image', type=str, required=True)
        args = parser.parse_args()
        model = args['model']
        #image_file = request.files['image']
        img_b64 = args['image']
        result = {}
        message = ''
        if model == 'ZKKTZS':
            result = recognition_zkktzs.imgFile_recognition(img_b64)
            code = 0
        else:
            message = 'The required model does not exist'
            code = 1
        data = {'result': result, 'code': code, 'message': message}
        # data_return = json.dumps(data, ensure_ascii=False)
        res = make_response(jsonify({'data': data}))
        res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Method'] = '*'
        res.headers['Access-Control-Allow-Headers'] = '*'
        return res
api.add_resource(Product, '/api/v1/AI_detect')
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)