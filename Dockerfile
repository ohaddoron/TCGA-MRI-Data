FROM python:3.8-slim

RUN apt update -y && apt upgrade -y && apt install -y libcurl4

WORKDIR /opt/project

COPY requirements.txt .

RUN pip install -r requirements.txt

