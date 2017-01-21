FROM python:3.5-alpine

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 \
  && apk del build-deps

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir -p /var/www/bullet-static
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

VOLUME ['/var/www/bullet-static']

ADD . /code/
