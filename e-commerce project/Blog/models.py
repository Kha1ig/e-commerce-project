from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from register.models import User
# Create your models here.

class Blog(models.Model):

    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_image/')
    created_add = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    short_description_1 = models.TextField(max_length=500)
    short_description_2 = models.TextField(max_length=500)
    short_description_3 = models.TextField(max_length=500)
    short_description_4 = models.TextField(max_length=500)
    short_description_5 = models.TextField(max_length=500)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy('Blog:blog-detail', args=[self.slug])

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200, blank=True, null=True)
    created_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Author (models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    STATUS_CHOICES = (
        ('reject', 'Reject'),
        ('approve', 'Approve'),
    )

    blog =  models.ForeignKey(Blog, on_delete=models.CASCADE)
    letter = models.TextField()
    name = models.CharField(max_length=100,)
    email = models.EmailField(max_length=127)
    date_add = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='reject')
    userprofile= models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment',blank=True,null=True)
    

    class Meta:
        ordering = ['-date_add']

    def __str__(self):
        return f'Comment {self.letter} by {self.name}'
    
    @property
    def comment_count(self):
        return self.letter.count()


