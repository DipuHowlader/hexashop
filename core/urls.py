from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('<slug:cat_name>/', views.Home.as_view(), name='home'),
    path('<slug:cat_name>/<slug:sub_cat>/', views.FilterProduct.as_view(), name='filterProduct'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('product/<int:pk>', views.Product.as_view(), name='product'),
    path('products/', views.Products.as_view(), name='products'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
]
