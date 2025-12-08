from django.apps import AppConfig


class PilkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pilk'

    def ready(self):
        import pilk.signals    

