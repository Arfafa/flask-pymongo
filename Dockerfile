FROM python:3.7-alpine

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install gunicorn
