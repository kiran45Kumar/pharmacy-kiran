from django.urls import path
from .views import login, index, contact, signup
urlpatterns = [
    path('index/<str:email>', index, name='index'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('contact/',contact, name='contact')
]