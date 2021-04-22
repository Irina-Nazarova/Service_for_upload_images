FROM python:3.8.5


COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD gunicorn img_app.wsgi:application --bind 0.0.0.0:8000