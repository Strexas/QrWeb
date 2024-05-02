"""
URL patterns for the 'constructor' app.

This module defines URL patterns for handling page-related views.

Attributes:
    urlpatterns (list): A list of URL patterns.
"""
from django.urls import path
from .views import PageUpdate, PageView

urlpatterns = [
    path('pages/<str:page_id>/edit', PageUpdate.as_view(), name='page_edit'),
    path('pages/<str:page_id>', PageView.as_view(), name='page_detail'),
]
