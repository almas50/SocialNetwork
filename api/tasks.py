import logging


from SocialNetwork.celery import app
from django.db.models import F


from .models import Page


@app.task
def update_page_visitors_counter(page_id):
    try:
        Page.objects.get(pk=page_id).contents.update(counter=F('counter') + 1)
    except Exception as error:
        logging.error(f'Exception while update page visitors counter {page_id} - {error}')
