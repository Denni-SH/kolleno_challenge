import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kolleno_coding_challenge.settings')
app = Celery('kolleno_coding_challenge')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
