from pickle import TRUE
from django.db import models

# Create your models here.

class CustomerModel(models.Model):
    #customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email= models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
    
