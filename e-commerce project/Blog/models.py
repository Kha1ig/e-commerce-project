from django.db import models
from django.urls import reverse_lazy

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
    short_description = models.CharField(max_length=200)
    created_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Author (models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

