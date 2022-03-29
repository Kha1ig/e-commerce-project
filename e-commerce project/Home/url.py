from django.urls import path
from Home.views import index

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),

]