from rest_framework import serializers
from firstapp.models import User , Product, OrderTabel ,Cartdetail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields='__all__'

class OrderTabelSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderTabel
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
