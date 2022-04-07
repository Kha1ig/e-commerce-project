from django.urls import path
from Shop.views import shop, shop_detail

app_name = 'Shop'

urlpatterns = [
    path('', shop,  name='shop'),
    path('<slug:slug>', shop_detail,  name='shop-detail'),

]