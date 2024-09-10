from celery import Celery
from celery.schedules import crontab

from webapp import create_app
from webapp.data_parser_site import get_data_from_drom, data_for_request

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def get_data_drom():
    with flask_app.app_context():
        get_data_from_drom()


def time_polling():
    with flask_app.app_context():
        try:
            time_polling = data_for_request().polling_interval + .0
            return time_polling
        except (TypeError, ValueError):
            return 60.0


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(time_polling(), get_data_drom.s())
    # sender.add_periodic_task(crontab(minute='*/5'), get_data_drom.s())

