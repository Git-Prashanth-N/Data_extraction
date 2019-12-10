FROM ubuntu:18.04

FROM python:3.7

MAINTAINER Prashanth Noothi "prashanthnoothi@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN apt-get install -y libsm6 libxext6 libxrender-dev tesseract-ocr

#RUN apt-get -y install tesseract-ocr

RUN pip install pillow pytesseract opencv-contrib-python

COPY * /APP
WORKDIR /APP

EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
