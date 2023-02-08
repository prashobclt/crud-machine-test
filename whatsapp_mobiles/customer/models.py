from django.db import models
from owner.models import Mobile

# Create your models here.
class Customer(models.Model):
    
    name = models.CharField(max_length=80)
    email= models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class Order (models.Model):
    mobile_details = models.ForeignKey(Mobile,on_delete=models.CASCADE)
    customer =  models.ForeignKey(Customer,on_delete=models.CASCADE)
