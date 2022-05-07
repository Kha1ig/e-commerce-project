from django.urls import path
# from Blog.views import blog, blog_detail
from .views import BlogListView, BlogDetailView, BlogCreateView ,BlogUpdateView, BlogDeleteView

app_name = 'Blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create-blog/', BlogCreateView.as_view(), name = 'create_blog'),
    path('<int:pk>/update-blog', BlogUpdateView.as_view(), name = 'update_blog'),
    path('<int:pk>/delete-blog', BlogDeleteView.as_view(), name = 'delete_blog'),
    path('<slug:slug>', BlogDetailView.as_view(), name='blog-detail'),

]