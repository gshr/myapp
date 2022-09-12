from pickle import TRUE
from django.db import models
from django.db.models import Count
from datetime import datetime
# Create your models here.

class CustomerModel(models.Model):
    #customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email= models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
    OrderDate = models.DateTimeField(default=datetime.now)
    
from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)