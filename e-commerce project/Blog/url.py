from django.urls import path
from Blog.views import blog, blog_detail

app_name = 'Blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('<slug:slug>', blog_detail, name='blog-detail'),

]