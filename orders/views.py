from django.shortcuts import render

# Create your views here.
def order(request):
    return render(request, 'orders/order.html', )
def cart(request):
    return render(request, 'orders/cart.html')