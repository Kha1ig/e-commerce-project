from django.contrib import admin
from Blog.models import Author, Blog, Category, Comment
# Register your models here.

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)