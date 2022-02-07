from django.db import models
from django.contrib.auth.models import User 




class sub_cat(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)


    def save(self, *args, **kwargs):
        prepare_url = self.title.replace(' ', '').replace('\'', '').lower()
        self.url = prepare_url
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    sub_cat = models.ManyToManyField(sub_cat)

    def __str__(self):
        return self.title



class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(default = '', upload_to = 'product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dis_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    in_stock = models.IntegerField()
    is_lattest = models.BooleanField(default=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class CartModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    

    @property
    def total (self):
        return (self.quantity * self.product.price)


    def __str__(self):
        return str(self.product)