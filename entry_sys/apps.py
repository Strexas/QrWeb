"""Used to define the configuration for entry_sys within a project"""
from django.apps import AppConfig


class RegSysConfig(AppConfig):
    """
       AppConfig subclass representing configuration for the 'entry_sys' Django application.

       Attributes:
       - default_auto_field: A string specifying the default primary key field type for models in the app.
                             In this case, it's set to 'django.db.models.BigAutoField'.
       - name: A string specifying the name of the Django application, in this case, 'entry_sys'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entry_sys'
