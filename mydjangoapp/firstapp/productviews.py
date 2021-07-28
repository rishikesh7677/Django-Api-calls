from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from firstapp.models import User,OrderTabel,Product,Cartdetail
from firstapp.Serializer import UserSerializer , ProductSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework import status

@api_view(['POST'])
def addproduct(request):
    if(request.method=='POST'):
        sr=ProductSerializer(data=request.data)
        if(sr.is_valid()):
            sr.save()
            return HttpResponse(sr.data,status=status.HTTP_201_CREATED)
        return HttpResponse(sr.errors,status=status.HTTP_400_BAD_REQUEST)