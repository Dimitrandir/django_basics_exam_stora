from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'STORA.accounts'

    def ready(self):
        import STORA.accounts.signals