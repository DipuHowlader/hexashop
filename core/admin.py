from django.contrib import admin
from .models import ProductModel, CartModel, Category, sub_cat

# Register your models here.


admin.site.register(ProductModel)
admin.site.register(Category)
admin.site.register(sub_cat)
admin.site.register(CartModel)
