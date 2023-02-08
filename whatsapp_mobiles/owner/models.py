from django.db import models

# Create your models here.
class Owner(models.Model):
        name = models.CharField(max_length = 80)
        password=models.CharField(max_length = 30)

class Mobile(models.Model):
        mobile_name = models.CharField(max_length=100)
        mobile_brand = models.CharField( max_length=50)
        mobile_rate = models.FloatField(default="")
        mobile_image = models.ImageField(upload_to='mobiles/')