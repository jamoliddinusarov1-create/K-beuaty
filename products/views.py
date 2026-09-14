from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    products = Product.objects.filter(in_stock=True)
    context= {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }

    return render(request, 'products/products_detail.html', context)