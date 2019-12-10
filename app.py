'''File name: app.py....................Author: Prashanth Noothi
   Date created: 16/11/2019.............Date last modified: 29/12/2019
   Python Version: 3.7 '''

# importing Flask from flask....................................

from flask import Flask

# Upload images to the folder...................................

UPLOAD_FOLDER = './'

# flask app requirements .......................................

application = Flask(__name__)
application.secret_key = "secret key"
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024 * 1024
