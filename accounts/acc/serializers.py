from dataclasses import fields
from rest_framework import serializers
from .models import *



class userregserializer(serializers.ModelSerializer):
    class Meta:
        model=userProfile
        fields='__all__'
        
        
        
class usercreateserializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields='__all__'
        
        
        
class usercartserializer(serializers.ModelSerializer):
    class Meta:
        model=UserCart
        fields='__all__'
        
        
class usercartproductserializer(serializers.ModelSerializer):
    class Meta:
        model=UserCartProduct
        fields='__all__'
        
class productserializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'
        
        
class productimgserializer(serializers.ModelSerializer):
    class Meta:
        model=product_image
        fields='__all__'