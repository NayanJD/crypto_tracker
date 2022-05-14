FROM python:3.9.10

ENV APP_HOME=/src

WORKDIR $APP_HOME

Add ./ /src

RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD ["gunicorn", "-b", "0.0.0.0", "crypto_tracker.wsgi"]
# CMD ["sleep", "infinity"]
