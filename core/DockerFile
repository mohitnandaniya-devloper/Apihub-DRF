
FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /core

COPY requirements.txt /core/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /core/

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver

