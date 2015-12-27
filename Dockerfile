FROM python:3.5.1

RUN mkdir /app
ADD src src

RUN pip install -r src/requirements.txt
RUN pip install gunicorn
RUN pip install -e src/.

EXPOSE 5000
RUN chmod +x src/run_celery.sh
RUN adduser --disabled-password --gecos '' celery_user
CMD gunicorn -w2 wsgi:app -b 0.0.0.0:5000