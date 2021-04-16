from flask import Flask, request
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

@app.route('/api/v1/AI_detect', methods=['POST', 'GET'])
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
            data_return = json.dumps(data)
            return data_return
        else:
            return 'The file format must be png, jpg, jpeg or gif.'
if __name__ == '__main__':
    app.run(debug=True)
'''
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
import json
import recognition_zkktzs
app = Flask(__name__)
api = Api(app)
# set arguments from

class Product(Resource):
    def get(self):
        return {'msg': 'Please use POST method'}
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('model', type=str)
        args = parser.parse_args()
        model = args['model']
        image_file = request.files['file']
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
api.add_resource(Product, '/api/v1/AI_detect')'''