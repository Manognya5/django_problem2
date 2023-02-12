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

    def update(self, instance, valid_data):
        instance.site_id = valid_data.get('site_id', instance.site_id)
        instance.site_name = valid_data.get('site_name', instance.site_name)
        instance.address = valid_data.get('address', instance.address)
        instance.city = valid_data.get('city', instance.city)
        instance.country = valid_data.get('country', instance.country)
        instance.zipcode = valid_data.get('zipcode', instance.zipcode)
        instance.save()
        return instance

    # def delete(instance, valid_data):
    #     Site.objects.get(instance=valid_data).delete()

    
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