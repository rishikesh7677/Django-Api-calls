from django.db import models
from datetime import datetime
#from django.contrib.postgres.fields import ArrayField
# Create your models here.
from django.utils import timezone

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email=models.EmailField()
    address=models.CharField(max_length=200)


class Product(models.Model):
    productid = models.CharField(max_length=30)
    price= models.IntegerField()
    quantity=models.IntegerField()
    description=models.CharField(max_length=200)


class OrderTabel(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    time=models.DateTimeField()
    status=models.CharField(max_length=200,default='Placed') 
    price=models.IntegerField()
    addres=models.TextField()

class Cartdetail(models.Model):
    orderid=models.ForeignKey(OrderTabel, on_delete=models.CASCADE)
    productid=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.IntegerField()
    statusofpd=models.CharField(max_length=200)
    expecteddate=models.DateTimeField(null=True)



