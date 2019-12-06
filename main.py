''''File name: main.py....................Author: Prashanth Noothi
   Date created: 16/11/2019.............Date last modified: 29/12/2019
   Python Version: 3.7 '''

# importing required libraries...........................................................
import os
import base64
from fyln import image_date
from flask import request, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
from io import BytesIO
from flask import Flask

# allowed extension files type............................................................
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# function for allowed files..............................................................
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

   
   
UPLOAD_FOLDER = './'

# flask app requirements .......................................

app = Flask(_name_)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024 * 1024 
# function for index ....................................................................
@app.route('/')
def index():
    return "Hello, World!"

# function for uploading a file..........................................................
@app.route('/file-upload', methods=['POST'])
def upload_file():
    filename = request.form['filename']
    file = request.form['file']

    file = Image.open(BytesIO(base64.b64decode(file)))

    # check if the post request has the file part
    if 'file' not in request.form:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    if filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(filename):
        filename = secure_filename(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        date = image_date(filename)
        resp = jsonify({'date': date})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp


# debugger for program.....................................................................

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug='True')
            
