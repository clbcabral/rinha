FROM python:alpine

WORKDIR /opt/app

RUN apk update && apk add postgresql-dev

ADD . .

RUN pip install -r requirements.txt

ENTRYPOINT /opt/app/entrypoint.sh