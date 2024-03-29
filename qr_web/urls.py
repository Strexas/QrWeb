"""
URL configuration for qr_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import typing

from django.contrib import admin
from django.urls import path, include,URLResolver,URLPattern
from django.conf.urls.static import static
from django.conf import  settings
from user_profile import views as user_profile_views
URL = typing.Union[URLPattern, URLResolver]
URLList = typing.List[URL]
urlpatterns: URLList = [
    path('admin/', admin.site.urls),
    path('', include('entry.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('profile/', include('user_profile.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
