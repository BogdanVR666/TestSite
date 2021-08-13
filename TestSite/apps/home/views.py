from django.shortcuts import render
from .models import Product

def home(request):
    profit_products = Product.objects.order_by('-price')
    return render(request, 'home/index.html', {'profit_products':profit_products})

def test(reqest):
    pass