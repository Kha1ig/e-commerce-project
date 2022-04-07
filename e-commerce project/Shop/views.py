from django.shortcuts import render
from .models import Product
# Create your views here.

def shop(request):
    shops = Product.objects.all()
    context = {
        'shops':shops
    }
    return render(request, 'category.html', context)


def shop_detail(request, slug):

    shop_detail = Product.objects.filter(slug=slug)

    context = {
        'shop_detail':shop_detail
    }

    return render(request, 'single-product.html', context)