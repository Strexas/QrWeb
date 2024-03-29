import user_profile.signals
"""This is apps file to register automatically profile pages"""
from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    """Class representing UserProfile"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'

    def ready(self):
        var = user_profile.signals
