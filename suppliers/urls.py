from django.urls import path
from .views import seller

urlpatterns = [
    path('sell/', seller, name='seller')
]