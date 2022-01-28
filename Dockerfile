FROM python:3.8-slim-buster

WORKDIR /scrapeguardian

RUN apt-get update && apt-get clean

RUN pip install --upgrade pip
COPY requirements.txt /scrapeguardian/requirements.txt
RUN pip install -r requirements.txt

COPY . /scrapeguardian