from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # create a function called ready()
    def ready(self):
        import users.signals
