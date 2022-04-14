from django.apps import AppConfig


class BroadcastConfig(AppConfig):
    name = 'broadcast'

def ready(self):
        from . import updater
        updater.start()