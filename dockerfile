FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app_be
# app_be: apliacacion backend
COPY . /app_be/

RUN pip install -r django_sorelle/requirements.txt