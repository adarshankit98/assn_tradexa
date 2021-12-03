from django.db import models

# Create your models here.
class GeeksModel(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField()
from django.contrib import admin
from .models import *


admin.site.register(Product)