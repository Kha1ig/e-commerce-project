"""my_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('Home.url', namespace='index')),
    path('shop/', include('Shop.url', namespace='Shop')),
    path('basket/', include('basket.url', namespace='basket')),
    path('blog/', include('Blog.url', namespace='Blog')),
    path('Contact/', include('Contact.url', namespace='contact')),
    path('register/', include('register.url', namespace='register')),
    
    path('tracking/', include('Pages.url', namespace='track')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

