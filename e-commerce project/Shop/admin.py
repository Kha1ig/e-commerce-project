from django.contrib import admin
from .models import Products, Categories, Brands

# Register your models here.

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Brands)
