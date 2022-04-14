from apscheduler.schedulers.background import BackgroundScheduler

from broadcast.views import broadcast_sms
#from .my_update import update_something


def start():
    #chose the scheduler depending on where you want to use it
    scheduler = BackgroundScheduler()
    scheduler.add_job(broadcast_sms, 'interval', seconds=10)
    scheduler.start()