from django.urls import path
from Contact.views import contact

app_name = 'contact'

urlpatterns = [
    path('', contact, name='contact'),
    

]