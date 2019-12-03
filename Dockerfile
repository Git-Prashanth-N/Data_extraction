FROM ubuntu:18.04

MAINTAINER Prashanth Noothi "prashanthnoothi@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN apt-get install -y libsm6 libxext6 libxrender-dev

RUN apt-get -y install tesseract-ocr

COPY . /app
WORKDIR /app

ADD package.json /app/package.json

RUN pip install pillow
RUN pip install pytesseract
RUN pip install opencv-contrib-python

EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
