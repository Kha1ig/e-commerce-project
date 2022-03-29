from django.urls import path
from register.views import register,login

app_name = 'register'

urlpatterns = [
    path('', register, name='register'),
    path('login', login, name='login'),

]