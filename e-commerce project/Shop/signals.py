from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from Shop.models import Product

User = get_user_model

def created_slug(instance, created ,*args ,**kwargs):
    if created:
        Product.objects.filter(id=instance.id).update(slug=slugify(instance.product_name))

post_save.connect(created_slug, sender = Product)