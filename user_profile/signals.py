"""This file is to make communication when user is created it
 will have profile page automatically"""
from  django.db.models.signals import post_save
from django.contrib.auth import models as auth_models
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=auth_models.User)
def create_profile(instance, created, **kwargs):
    """Signal when creating profile"""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=auth_models.User)
def save_profile(instance, **kwargs):
    """Create and save profile"""
    instance.profile.save()
