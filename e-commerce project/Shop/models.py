from django.db import models
from django.urls import reverse_lazy
from ckeditor_uploader.fields import RichTextUploadingField
from register.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Products(models.Model):

    STATUS_CHOICES = (
        ('no information', 'No information'),
        ("product doesn't exsist", "Product doesn't exsist"),
        ('in Stock', 'In Stock'),
    )
    STATUS_CHOICE = (
        ('without touch of hand', 'Without touch of hand'),
    )
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product-image')
    image_1 = models.ImageField(upload_to='product-image')
    image_2 = models.ImageField(upload_to='product-image')
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    brand = models.ForeignKey('Brands', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='no information')
    short_description = models.TextField()
    description_1 = RichTextUploadingField()
    description_2 = RichTextUploadingField()
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
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category = category_id)
        else:
            return Products.get_all_products()
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
    
class Categories(models.Model):
    category_name = models.CharField(max_length=100)

    @staticmethod
    def get_all_categories():
        return Categories.objects.all()

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class Brands(models.Model):
    brand_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.brand_name
    
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
