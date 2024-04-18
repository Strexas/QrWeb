"""
URL patterns for the 'constructor' app.

This module defines URL patterns for handling page-related views.

Attributes:
    urlpatterns (list): A list of URL patterns.
"""
from django.urls import path
from .views import PageUpdate, PageView

urlpatterns = [
    path('pages/<int:pk>/edit', PageUpdate.as_view(), name='page_edit'),
    path('pages/<int:pk>', PageView.as_view(), name='page_detail'),
]
