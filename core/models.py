from distutils.command.upload import upload
from django.db import models



class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(default = '', upload_to = 'product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dis_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    in_stock = models.IntegerField()
    cat_choices = [
        ('men', 'men'),
        ('wahmen','women'),
        ('kid','kid\'s'),

    ]
    is_lattest = models.BooleanField(default=True)

    catagory = models.CharField(max_length=6, choices=cat_choices)


    def __str__(self):
        return self.name