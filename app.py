'''File name: app.py....................Author: Prashanth Noothi
   Date created: 16/11/2019.............Date last modified: 29/12/2019
   Python Version: 3.7 '''

# importing Flask from flask....................................

from flask import Flask

# Upload images to the folder...................................

UPLOAD_FOLDER = './'

# flask app requirements .......................................

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
