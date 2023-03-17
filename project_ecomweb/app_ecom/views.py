from django.shortcuts import render
from .forms import ProductAddForm

# Create your views here.

# dashboard
def dashboard_index(request):
    return render(request, 'dashboard/dashboard.html')

# products
def product_add(request):
    add_product = ProductAddForm()
    context = {"form": add_product}
    return render(request, 'products/product_add.html', context)

def product_index(request):
    return render(request, 'products/product_index.html')