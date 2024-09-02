from django.urls import path
from .views import medicines,create

urlpatterns = [
    path("medicines/", medicines, name='medicines'),
    path('create/', create, name='create')
]