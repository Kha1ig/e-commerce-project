from django.contrib import admin
from .models import Filter_price, Products, Categories, Brands,Colours

# Register your models here.

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Brands)
admin.site.register(Colours)
admin.site.register(Filter_price)


