import os
import base64
from fyln import image_date
from flask import request, jsonify
from werkzeug.utils import secure_filename

from PIL import Image
from io import BytesIO

from app import app

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return "Hello, World!"


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


if __name__ == "__main__":
    app.run(debug=True)