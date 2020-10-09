from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'home.html', context)

def product(request, pk):
    product = get_object_or_404(Product ,id=pk)

    context = {
        'product': product
    }
    return render(request, 'product.html', context)

def checkout(request):
    return render(request, 'checkout.html')
