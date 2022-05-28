from django.urls import path
from .views import blog_api_view

urlpatterns = [
    path('blog', blog_api_view)
]