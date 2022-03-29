from django.shortcuts import render

# Create your views here.

def shop(request):

    return render(request, 'category.html')


def shop_detail(request):

    return render(request, 'single-product.html')