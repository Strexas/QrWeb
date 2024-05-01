"""URL configuration for qr_web project."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('change_image/', views.change_image, name='change_image'),
    path('delete_image/', views.delete_image, name='delete_image'),
    path('create_page/', views.create_page, name='create_page'),
    path('view_page/<int:page_id>/', views.view_page, name='view_page'),
    path('delete_page/<int:page_id>/', views.delete_page, name='delete_page'),
]
