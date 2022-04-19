import math
from django.shortcuts import render
from Blog.forms import CommentForm
from Blog.models import Blog, Comment
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import get_user_model

User=get_user_model()


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

@csrf_exempt
def blog_detail(request, slug):

    blog = Blog.objects.filter(slug=slug).first()
    new_comment = Comment.objects.filter(blog=blog,status='approve')

    forum = CommentForm()
    if User.is_authenticated:
        if request.method == 'POST':
            Comment.objects.create(
                blog = Blog.objects.all().filter(slug=slug).first(),
                letter = request.POST.get('letter'),
                name = request.POST.get('name'),
                email = request.POST.get('email'),
            )
    
    
    context = {
        'blog': blog,
        'forum': forum,
        'new_comment': new_comment,
    }

    return render(request, 'single-blog.html', context=context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Blog.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=Comment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= Comment.objects.get(sno=parentSno)
            comment=Comment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")