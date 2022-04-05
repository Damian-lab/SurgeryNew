from apscheduler.schedulers.background import BackgroundScheduler
from .my_update import update_something


def start():
    #chose the scheduler depending on where you want to use it
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_something, 'interval', seconds=10)
    scheduler.start()