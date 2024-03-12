"""URL configuration for qr_web project."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]