"""This file is for registering admin page content"""
from django.contrib import admin
from .models import Profile,Page
admin.site.register(Profile)
admin.site.register(Page)
