FROM python:3.8.5

WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
CMD gunicorn img_app.wsgi:application --bind 0.0.0.0:8000