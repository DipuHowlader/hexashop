from asyncio.windows_events import NULL
from django.shortcuts import render
from django.views import View
from .models import ProductModel

# Create your views here.


class Home(View):
    def get(self, request, *args, **kwargs):
        products = ProductModel.objects.all()
        return render(request, 'index.html', {'products':products})

class Cart(View):
    def get(self, request, *args, **kwargs):
        products = ProductModel.objects.all()
        return render(request, 'cart.html', {'cart':products})

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')

class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')


class Product(View):
    def get(self, request,  pk, *args, **kwargs):
        product = ProductModel.objects.get(id = pk)
        return render(request, 'product.html', {'product': product})


class Products(View):
    def get(self, request, *args, **kwargs):
        products = ProductModel.objects.all()
        return render(request, 'products.html',{'products': products})

