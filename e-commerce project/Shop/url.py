from django.urls import path
from Shop.views import shop, shop_detail, updateItem, cart, checkout

app_name = 'Shop'

urlpatterns = [
    path('', shop,  name='shop'),
    path('update_item/', updateItem, name='update_item'),
    path('<slug:slug>', shop_detail,  name='shop-detail'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),

]