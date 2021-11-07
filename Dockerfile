FROM python:3.8.0-alpine

WORKDIR /cbv

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libmagic jpeg-dev zlib-dev

COPY requirements.txt /cbv/
RUN pip install -r requirements.txt

COPY . /cbv/
