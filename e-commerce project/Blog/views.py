import math
from django.shortcuts import render
from Blog.models import Blog

# Create your views here.

def blog(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    per_count = 2
    all_blogs = Blog.objects.all().count()
    blogs = Blog.objects.all()[per_count * (page -1):(page * per_count)]
    total_page_count = math.ceil(all_blogs / per_count)
    previous_page = page - 1 if not page == 1 else page
    next_page = page + 1 if not page == total_page_count else page
    page_range = range(1, total_page_count + 1)

    current_page = page

    #blogs = Blog.objects.all()

    context = {
        'blogs':blogs,
        'current_page': current_page,
        'previous_page': previous_page,
        'next_page': next_page,
        'page_range': page_range,

    }

    return render(request, 'blog.html', context)

def blog_detail(request, slug):

    blog = Blog.objects.filter(slug=slug).first()

    return render(request, 'single-blog.html', {'blog': blog})