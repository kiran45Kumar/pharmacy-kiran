from django.urls import path
from .views import order, cart
urlpatterns = [
    path('order/', order, name='order'),
    path('cart/', cart, name='cart')
]