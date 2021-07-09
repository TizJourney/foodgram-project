FROM python:3.8.5

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY nginx.conf /etc/nginx/nginx.conf

RUN python manage.py collectstatic --no-input

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000 --error-logfile=errors.log 
