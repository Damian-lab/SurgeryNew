from django.apps import AppConfig


class AppointmentConfig(AppConfig):
    name = 'appointment'
    
   
def ready(self):
        from . import updater
        updater.start()