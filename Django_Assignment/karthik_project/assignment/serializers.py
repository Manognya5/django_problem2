from rest_framework import serializers
from .models import *
from django.db.models import fields

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Details
        fields=['user_id','first_name','last_name','address','state','country','zipcode']
        abstraction=True

    def create(self,validated_data):
        return Details.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.user_id=validated_data.get('user_id',instance.user_id)
        instance.first_name=validated_data.get('first_name',instance.first_name)
        instance.last_name=validated_data.get('last_name',instance.last_name)
        instance.address=validated_data.get('address',instance.address)
        instance.state=validated_data.get('state',instance.state)
        instance.country=validated_data.get('country',instance.country)
        instance.zipcode=validated_data.get('zipcode',instance.zipcode)
        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['order_id','product_name','price','payment_status']
        
    def create(self,validated_data):
        return Details.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.order_id=validated_data.get('order_id',instance.order_id)
        instance.product_name=validated_data.get('product_name',instance.product_name)
        instance.price=validated_data.get('price',instance.price)
        instance.payment_status=validated_data.get('payment_status',instance.payment_status)
        instance.save()
        return instance
