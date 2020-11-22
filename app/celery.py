import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app', include=['api.tasks'])

app.conf.update(
    task_serializer='json',
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)