from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'index.html')

def list_products(request):
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)

    products = Product.objects.all()
    product_paginator=Paginator(products, 12)
    products=product_paginator.get_page(page)
    return render(request, 'products.html', {'products' : products})

def product_details(request):
    return render(request, 'product_details.html')