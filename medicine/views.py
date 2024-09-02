from django.shortcuts import render
# from .models import Medicine
# Create your views here.
def medicines(request):
    return render(request, 'medicine/medicine.html')
def create(request):
    return render(request, 'medicine/create.html')