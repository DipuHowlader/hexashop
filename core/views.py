from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import ProductModel, CartModel, Category, sub_cat
import json


class Home(View):
    def get(self, request, *args, **kwargs):
        current_cat =  self.kwargs['cat_name']
        products = ProductModel.objects.all()
        cat = Category.objects.all()
        try:
            active_cat= Category.objects.get(title = current_cat)
            sub_category = active_cat.sub_cat.all()
        except:
            sub_category = []
            active_cat = []
        return render(request, 'index.html', {'products':products,'cat' :cat, 'sub_cat' :sub_category})

class FilterProduct(View):
    def get(self, request, *args, **kwargs):
        products = ProductModel.objects.all()

       
        return render(request, 'filter-product.html', {'products':products})


class Cart(View):
    def get(self, request, *args, **kwargs):
        try:
            if request.user:
                carts = CartModel.objects.filter(user = request.user)
        except:
            carts = []
        return render(request, 'cart.html', {'carts':carts})

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        action =data['form_type']
        cart_item =  data['product']
        cart_to_update = CartModel.objects.get(id=cart_item)
        if action == 'increase_qunatity':
            cart_to_update.quantity += 1
            cart_to_update.save()

        if action == 'decrease_qunatity':
            cart_to_update.quantity -= 1
            cart_to_update.save()

        if action == 'delete_cart':
            cart_to_update.delete()
        try:
            if request.user:
                carts = CartModel.objects.filter(user = request.user)
        except:
            carts = []
        return render(request, 'cart.html', {'carts':carts})

       
       

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
    
    def post(self, request,  pk, *args, **kwargs):
        if self.request.POST.get('form_type') == 'add_to_cart':
            quantity = self.request.POST.get('quantity')
            product = self.request.POST.get('product')
            product_instance = get_object_or_404(ProductModel, id = product)
            CartModel.objects.get_or_create(product = product_instance, user = request.user, quantity=quantity)

        product = ProductModel.objects.get(id = pk)
        return render(request, 'product.html', {'product': product})


class Products(View):
    def get(self, request, *args, **kwargs):
        products = ProductModel.objects.all()
        return render(request, 'products.html',{'products': products})


class Checkout(View):
    def get(self, request, *args, **kwargs):
        products = ProductModel.objects.all()
        return render(request, 'products.html',{'products': products})


