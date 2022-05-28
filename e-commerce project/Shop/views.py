from django.shortcuts import render
from django.http import JsonResponse
from .models import Colours, Filter_price, Products, Categories, Brands, Order, OrderItem
import json

# Create your views here.

def shop(request):
    # categories = Categories.objects.all()
    #shops = Products.objects.all()
    categories = Categories.objects.all()
    brand = Brands.objects.all()
    colour = Colours.objects.all()
    filter_price = Filter_price.objects.all()
    products = None
    order = {'get_cart_total':0, 'get_cart_items':0}
    cartItems = order['get_cart_items']
    CATID = request.GET.get('category')
    brandID = request.GET.get('brand')
    colourID = request.GET.get('colour')
    priceID = request.GET.get('price')
    AtoZID = request.GET.get('AtoZ')
    ZtoAID = request.GET.get('ZtoA')
    if CATID:
        products = Products.objects.filter(category=CATID)
    elif brandID:
        products = Products.objects.filter(brand=brandID)
    elif colourID:
        products = Products.objects.filter(colour=colourID)
    elif priceID:
        products = Products.objects.filter(filter_price=priceID)
    elif AtoZID:
        products = Products.objects.all().order_by('product_name')
    elif ZtoAID:
        products = Products.objects.all().order_by('-product_name')
    
    else:
        products = Products.objects.all()

    context = {
        #'shops':shops,
        'categories': categories,
        'brand': brand,
        'products': products,
        'order': order,
        'cartItems': cartItems,
        'colour': colour,
        'filter_price': filter_price,
    }
    return render(request, 'category.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	user = request.user
	product = Products.objects.get(id=productId)
	order, created = Order.objects.get_or_create(user=user, complete=False)

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

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = Order.OrderItem_set.all()
        cartItems = order['get_cart_items']
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    
    context = {
        'items':items, 
        'order':order,
        'cartItems': cartItems
        }
    return render(request, 'cart.html', context)

def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete = False)
        items = Order.OrderItem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    
    context = {'items':items, 'order':order,}
    return render(request, 'checkout.html', context)