web: pipenv rub python manage.py runserver 0.0.0.0:$PORT
web: gunicorn core.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
