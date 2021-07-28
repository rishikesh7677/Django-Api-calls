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
from firstapp import ordertabelcontroller,cartdetailveiw
from django import db
db.connections.close_all()

@api_view(['GET','POST'])
def index(request):
    if(request.method=='GET'):
        return HttpResponse("Hi First Api Hits")

    if(request.method=='POST'):
        sr=UserSerializer(data=request.data)
        if(sr.is_valid()):
            sr.save()
            #print(type(sr),sr['email'])
            return HttpResponse(sr.data,status=status.HTTP_201_CREATED)
        return HttpResponse(sr.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET'])
def cancel(request,ordid,prodid):
    cart=ordertabelcontroller.getcartitem(ordid, prodid)
    if(type(cart)!=Cartdetail):
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if(request.method=='GET'):
        return HttpResponse(cart.statusofpd,status=status.HTTP_200_OK)
    else:
        cart.statusofpd='Cancelled'
        cart.save() 
        #write.query for carttabel
        return HttpResponse(cart.statusofpd,status=status.HTTP_201_CREATED) 


@api_view(['PUT'])    
def updatestatus(request,ordid,prodid):
    cart=ordertabelcontroller.getcartitem(ordid, prodid)
    if(type(cart)!=Cartdetail):
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    cart.statusofpd=request.data['status']
    cart.save() 
    #write.query for carttabel
    return HttpResponse(cart.statusofpd,status=status.HTTP_201_CREATED)


    '''
     query=Cartdetail.objects.raw("Select * from cartdetails where orderid=x")
     query=OrderTabel.objects.raw("select count * from ordertabel where MONTH(time)=x)
     '''

@api_view(['POST'])
def addorder(request):
    datax=request.data 
    prodid=datax['productid']
    userid=datax['userid']
    del datax['productid']
    del datax['userid']
    datax['time']=timezone.now()
    datax['status']='Placed'
    response=(ordertabelcontroller.fullfilorder(prodid,userid))
    if(type(response)!=str):
        datax['userid']=response.id
        sr=OrderTabelSerializer(data=datax)
        if(sr.is_valid()):
            x=sr.save()
            cartdetailveiw.addcartitem(prodid,x)
            return HttpResponse(sr.data,status=status.HTTP_201_CREATED)
        return HttpResponse(sr.errors,status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)



