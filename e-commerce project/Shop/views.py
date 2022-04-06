from django.shortcuts import render
from .models import Product
# Create your views here.

def shop(request):
    shops = Product.objects.all()
    context = {
        'shop':shops
    }
    return render(request, 'category.html', context=context)


def shop_detail(request):

    return render(request, 'single-product.html')