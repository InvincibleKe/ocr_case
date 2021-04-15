from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import json
import recognition_zkktzs
app = Flask(__name__)
api = Api(app)
# set arguments from
parser = reqparse.RequestParser()
parser.add_argument('image')
parser.add_argument('model', type=str)
class Product(Resource):
    def get(self):
        return {'msg': 'Please use POST method'}
    def post(self):
        args = parser.parse_args()
        model = args['model']
        image_file = args['image']
        result = {}
        message = ''
        if model == 'ZKKTZS':
            result = recognition_zkktzs.imgFile_recognition(image_file)
            code = 1
        else:
            message = 'The required model does not exist'
            code = 0
        data = {'result': result, 'code': code, 'message': message}
        data_return = json.dumps(data)
        return data_return
api.add_resource(Product, '/api/v1/AI_detect')