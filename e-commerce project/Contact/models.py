from django.db import models

# Create your models here.

class Contact_info(models.Model):
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=127)
    days_open = models.CharField(max_length=127)
    email = models.EmailField(max_length=127)
    short_text = models.CharField(max_length=100)

class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=127)
    email = models.EmailField(max_length=127)
    subject = models.CharField(max_length=127)

