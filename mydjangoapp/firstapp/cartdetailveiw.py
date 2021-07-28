from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse 
from firstapp.models import User,OrderTabel,Product,Cartdetail
from firstapp.Serializer import UserSerializer,OrderTabelSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework import status
from firstapp import ordertabelcontroller
from django import db
db.connections.close_all()

def addcartitem(prlist,ordid):
    for  prid,q in prlist:
        prd=Product.objects.get(productid=prid)
        #print(ordid,prd.pk)
        n=Cartdetail.objects.create(orderid=ordid,productid=prd,quantity=q,
        price=q*prd.price,statusofpd="Placed")
        n.save()