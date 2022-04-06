from django.shortcuts import render
from Blog.models import Blog

# Create your views here.

def blog(request):
    blogs = Blog.objects.all()

    return render(request, 'blog.html', {'blogs':blogs})

def blog_detail(request, slug):

    blog = Blog.objects.filter(slug=slug)

    return render(request, 'single-blog.html', {'blog': blog})