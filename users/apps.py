from django.apps import AppConfig
from constant import USERS

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = USERS

    def ready(self):
        import users.signals