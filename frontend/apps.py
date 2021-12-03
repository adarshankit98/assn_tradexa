from django.apps import AppConfig

from ecom.settings import INSTALLED_APPS


class FrontendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'frontend'

INSTALLED_APPS = [
    'frontend.apps.FrontendConfig'
]