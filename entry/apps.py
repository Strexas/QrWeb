"""Used to define the configuration for entry within a project"""
from django.apps import AppConfig


class RegSysConfig(AppConfig):
    """
       AppConfig subclass representing configuration for the 'entry' Django application.

       Attributes:
       - default_auto_field: String specify the default primary key type for models in the app.
                             In this case, it's set to 'django.db.models.BigAutoField'.
       - name: A string specifying the name of the Django application, in this case, 'entry'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entry'
