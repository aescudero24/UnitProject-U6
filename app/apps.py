from django.apps import AppConfig


class Config(AppConfig):
    name = "app"

    def ready(self):
    	import app.signals