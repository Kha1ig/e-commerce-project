from django.contrib import admin

from Contact.models import Contact, Contact_info

# Register your models here.

admin.site.register(Contact)
admin.site.register(Contact_info)