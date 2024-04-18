"""This is apps file to register automatically constructor"""
from django.apps import AppConfig


class ConstructorConfig(AppConfig):
    """
    AppConfig subclass for configuring the 'constructor' app.

    This class defines configuration settings for the 'constructor' app.
    It specifies the default auto field and the name of the app.

    Attributes:
    default_auto_field (str): The default auto field to use for model primary keys.
    name (str): The name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'constructor'
