from rest_framework import serializers
from .models import *

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

        def create(self, validated_data):
            site = Site (
                site_id=validated_data['site_id'],
                site_name=validated_data['username'],
                address=validated_data['address'],
                state=validated_data['state'],
                country=validated_data['country'],
                zipcode=validated_data['zipcode']
            )
            site.save()
            return site
            

        def update(self, instance, validated_data):
            instance.site_id = validated_data.get('site_id', instance.site_id)
            instance.site_name = validated_data.get('site_name', instance.site_name)
            instance.address = validated_data.get('address', instance.address)
            instance.state = validated_data.get('state', instance.state)
            instance.country = validated_data.get('country', instance.country)
            instance.zipcode = validated_data.get('zipcode', instance.zipcode)
            instance.save()
            return instance
        

class IAPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IAP
        fields = '__all__'

class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'