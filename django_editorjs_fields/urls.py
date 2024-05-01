"""URL configuration for Editor.js related views."""
from django.urls import path

from .views import ImageByUrl, ImageUploadView, LinkToolView

urlpatterns = [
    path(
        'image_upload/',
        ImageUploadView.as_view(),
        name='editorjs_image_upload',
    ),
    path(
        'linktool/',
        LinkToolView.as_view(),
        name='editorjs_linktool',
    ),
    path(
        'image_by_url/',
        ImageByUrl.as_view(),
        name='editorjs_image_by_url',
    ),
]
