FROM python:3.10.5-slim-buster
WORKDIR /todoapi
COPY . .
RUN pip install -r requirements.txt
RUN rm db.sqlite3 ; exit 0
RUN python manage.py migrate
ENV DJANGO_SUPERUSER_PASSWORD admin
RUN python manage.py createsuperuser --no-input --username admin --email admin@admin.com
EXPOSE 8000
