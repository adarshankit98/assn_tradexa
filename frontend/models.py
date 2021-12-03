from django.contrib import admin
# from .models import *
from django.db import models


# admin.site.register('products')
class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # description = models.TextField()
    # image = models.CharField(max_length=5000, null=True, blank=True)
    weight = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

