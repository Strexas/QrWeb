
"""This is apps file to register automatically profile pages"""
from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    """Class representing UserProfile"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile'

    def ready(self):
        # pylint: disable=import-outside-toplevel, unused-import
        import profile.signals
