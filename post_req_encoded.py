'''File name: post_req_encoded.py....................Author: Prashanth Noothi
   Date created: 16/11/2019.............Date last modified: 29/12/2019
   Python Version: 3.7 '''

# importing required libraries...................................................
import requests
from PIL import Image
import base64
import sys


# function for make post req for base64..........................................
def make_post_req_base64(filename):
    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    # defining the api-endpoint..................................................
    API_ENDPOINT = "http://127.0.0.1:5000/file-upload"

    # print(filename, width, height)

    # data to be sent to api......................................................
    data = {'filename': filename,
            'file': encoded_string}

    # sending post request and saving response as response object.................
    r = requests.post(url=API_ENDPOINT, data=data)

    # extracting response text....................................................
    print(r.text)


# unit testing for particular function ...........................................
if __name__ == '__main__':
    if (len(sys.argv) > 1):
        make_post_req_base64(sys.argv[1])

    else:
        print("No image filename mentioned!!")
