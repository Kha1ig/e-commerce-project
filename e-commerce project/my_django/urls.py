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

from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace='social')),  # <--
    path('', include('Home.url', namespace='index')),
    path('shop/', include('Shop.url', namespace='Shop')),
    
    path('Contact/', include('Contact.url', namespace='contact')),
    path('register/', include('register.url', namespace='register')),
    path('api/', include('Blog.api.urls')),
    path('tracking/', include('Pages.url', namespace='track')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path('blog/', include('Blog.url', namespace='Blog')),
)