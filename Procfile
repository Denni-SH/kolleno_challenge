web: celery -A kolleno_coding_challenge worker --loglevel=info & python manage.py migrate && gunicorn kolleno_coding_challenge.wsgi  --bind 0.0.0.0:$PORT
