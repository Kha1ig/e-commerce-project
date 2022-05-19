from django.shortcuts import render
from django.http import JsonResponse
from .models import Products, Categories, Brands, Order, OrderItem, Customer
import json
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

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Products.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)




def shop_detail(request, slug):

    shop_detail = Products.objects.filter(slug=slug)

    context = {
        'shop_detail':shop_detail
    }

    return render(request, 'single-product.html', context)


def cart(request):

    return render(request, 'cart.html')

def checkout(request):

    return render(request, 'checkout.html')