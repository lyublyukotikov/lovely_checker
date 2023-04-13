from lovely_checker.celery import app
from moderation.service import send_item_mail, send_city_mail, \
    send_item_success_mail, send_user_failure_mail


@app.task()
def send_city_moderation_mail(*args, **kwargs):
    send_city_mail(*args, **kwargs)
    return "Done"


@app.task()
def send_item_moderation_mail(*args, **kwargs):
    send_item_mail(*args, **kwargs)
    return "Done"


@app.task()
def send_item_success_moderation_mail(*args, **kwargs):
    send_item_success_mail(*args, **kwargs)
    return "Done"


@app.task()
def send_user_failure_moderation_mail(*args, **kwargs):
    send_user_failure_mail(*args, **kwargs)
    return "Done"
