"""
URL patterns for the 'constructor' app.

This module defines URL patterns for handling post-related views.

Attributes:
    urlpatterns (list): A list of URL patterns.
"""
from django.urls import path
from .views import PostUpdate, PostView

urlpatterns = [
    path('posts/<int:pk>/edit', PostUpdate.as_view(), name='post_edit'),
    path('posts/<int:pk>', PostView.as_view(), name='post_detail'),
]
