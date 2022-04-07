from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Product(models.Model):

    STATUS_CHOICES = (
        ('no information', 'No information'),
        ("product doesn't exsist", "Product doesn't exsist"),
        ('in Stock', 'In Stock'),
    )
    STATUS_CHOICE = (
        ('without touch of hand', 'Without touch of hand'),
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product-image')
    image_1 = models.ImageField(upload_to='product-image')
    image_2 = models.ImageField(upload_to='product-image')
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='no information')
    short_description = models.TextField()
    description_1 = models.TextField()
    description_2 = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()
    Depth = models.IntegerField()
    Weight = models.IntegerField()
    guarantee = models.CharField(max_length=50)
    packeting = models.CharField(max_length=100, choices=STATUS_CHOICE, default='without touch of hand')
    freshness_duration = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy('Shop:shop-detail', args=[self.slug])

    def __str__(self):
        return self.product_name
    
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.brand_name
