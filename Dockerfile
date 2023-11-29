FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN python manage.py migrate
