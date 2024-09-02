from django.shortcuts import render,redirect
from .models import Customer
import time
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.views.generic.base import TemplateView
# Create your views here.

def signup(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('input')
        name = request.POST.get('Name')
        phone = request.POST.get('phone')
       
        if not email:
            msg = 'Enter Your Email'
        elif not password:
            msg = 'Enter Your Password'
        elif not name:
            msg = 'Enter Your Email'
        elif not phone:
            msg = 'Enter Your Phone no'
        else:
            hashed_password = make_password(password)
            Customer.objects.create(email = email, password = hashed_password, name = name, phone = phone)
            msg = 'Success'
            time.sleep(5)
            return redirect('login')
  
    return render(request, 'customer/signup.html', {"msg":msg})
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('input')
        try:
            customer = Customer.objects.get(email = email)
            if check_password(password, customer.password):
                return redirect('index', email = email)
        except Customer.DoesNotExist:
            messages.error(request, 'Invalid credentials')
            
    return render(request,'customer/login.html')
def index(request,email):
    user = Customer.objects.get(email = email)
    return render(request, 'customer/index.html',{'name':user.name})
def contact(request):
    return render(request, 'customer/contact.html')
class view_staff(TemplateView):
    template_name = 'view_staff.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userdata = Customer.objects.all()
        context ={"userdata":userdata}
