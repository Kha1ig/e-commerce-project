from django.db import models
from django.urls import reverse_lazy
from ckeditor_uploader.fields import RichTextUploadingField
from register.models import User

# Create your models here.

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
    colour = models.ForeignKey('Colours', on_delete=models.CASCADE, blank=True, null=True)
    width = models.IntegerField()
    height = models.IntegerField()
    Depth = models.IntegerField()
    Weight = models.IntegerField()
    guarantee = models.CharField(max_length=50)
    packeting = models.CharField(max_length=100, choices=STATUS_CHOICE, default='without touch of hand')
    freshness_duration = models.CharField(max_length=30)
    filter_price = models.ForeignKey('Filter_price', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy('Shop:shop-detail', args=[self.slug])

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'



class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
    

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 
    

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
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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

class Colours(models.Model):
    colour_name = models.CharField(max_length=100)

    def __str__(self):
        return self.colour_name

    class Meta:
        verbose_name = 'Colour'
        verbose_name_plural = 'Colours'

class Filter_price(models.Model):
    
    FILTER_PRICE = (
        ('10 to 30', '10 to 30'),
        ('30 to 50', '30 to 50'),
        ('50 to 100', '50 to 100')
    )

    price = models.CharField(choices=FILTER_PRICE, max_length=100)

    def __str__(self):
        return self.price