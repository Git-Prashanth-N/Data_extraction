FROM ubuntu:18.04

FROM python:3.7

RUN apt-get update && apt-get install -y \
	wget \
	unzip \
	git

# Install dependencies
RUN apt-get install -y build-essential libgtk2.0-dev cmake python-dev python-numpy libeigen3-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev default-jdk ant
# Install pip
RUN wget https://bootstrap.pypa.io/get-pip.py

RUN python get-pip.py && rm get-pip.py

RUN pip install --upgrade pip

RUN pip install opencv-contrib-python

RUN pip install Pillow 

RUN apt-get install libjpeg62-turbo-dev

COPY . /APP
WORKDIR /APP

EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
