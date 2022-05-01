from django.urls import path
# from Blog.views import blog, blog_detail
from .views import BlogListView, BlogDetailView

app_name = 'Blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('<slug:slug>', BlogDetailView.as_view(), name='blog-detail'),

]