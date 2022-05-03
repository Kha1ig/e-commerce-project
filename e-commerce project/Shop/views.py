from unicodedata import category
from django.shortcuts import render
from .models import Products, Categories, Brands
# Create your views here.

def shop(request):
    # categories = Categories.objects.all()
    brand = Brands.objects.all()
    #shops = Products.objects.all()
    products = None
    categories = Categories.get_all_categories()

    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();


    context = {
        #'shops':shops,
        'categories': categories,
        'brand': brand,
        'products': products
    }
    return render(request, 'category.html', context)


def shop_detail(request, slug):

    shop_detail = Products.objects.filter(slug=slug)

    context = {
        'shop_detail':shop_detail
    }

    return render(request, 'single-product.html', context)