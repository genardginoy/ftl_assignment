from django.apps import AppConfig


class FtlAppConfig(AppConfig):
    name = 'ftl_app'

    def ready(self):
    	import ftl_app.signals
