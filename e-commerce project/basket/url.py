from django.urls import path
from basket.views import cart, checkout

app_name = 'basket'

urlpatterns = [
    path('', cart, name='basket'),
    path('checkout/', checkout, name='checkout'),

]