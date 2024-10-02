from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def shop(request):
    return render(request, 'shop.html')

def index(request):
    return render(request, 'cart.html')

def services(request):
    return render(request, 'services.html')


