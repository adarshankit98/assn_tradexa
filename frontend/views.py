from django.shortcuts import render
from .models import *
# from .products import *

def products(request):
    productss = Product.objects.all()
    return render(request, 'products.html', {'productss':productss})