from firstapp.models import User,Product
# Create your views here.
from django.http import HttpResponse
from rest_framework import filters
from rest_framework import status
from firstapp.models import User,OrderTabel,Product,Cartdetail
class Error(Exception):
    """Base class for other exceptions"""
    pass
class Lessquantity(Error):
    pass 

def fullfilorder(prlist,userid):
    try:
        usr=User.objects.get(pk=userid)
    except User().DoesNotExist:
        return "User Does Not Exist"

    listofpr=[]
    for idx,q in prlist:
        try:
            prod=Product.objects.get(productid=idx)
        except Product().DoesNotExist:
            return "Product Not Exist"
        except Lessquantity:
            return "Not Enough Quantity"
        prod.quantity-=q
        listofpr.append(prod)
    for pr in listofpr:
        pr.save()
    return usr

def getcartitem(ordid,prodid):
    try:
        order= OrderTabel.objects.get(pk=ordid)
        prod=Product.objects.get(pk=prodid)
        cart=Cartdetail.objects.get(orderid=order,productid=prod)
    except OrderTabel().DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    except Product().DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    except Cartdetail().DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    return cart
