FROM python:3.5-alpine

WORKDIR /opt/bullet

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && apk add libevent \
  && pip install psycopg2 gevent \
  && apk del build-deps

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /var/www/bullet-static

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

VOLUME ["/var/www/static"]
EXPOSE 80
