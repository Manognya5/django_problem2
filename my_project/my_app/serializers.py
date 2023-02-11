from rest_framework import serializers
from .models import * 


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Retailer
        fields='__all__'
        abstraction=True

        def create(self, validated_data):
            retailer=Retailer(
                person_id=validated_data['person_id'],
                person_name=validated_data['person_name'],
                address=validated_data['address'],
                state=validated_data['state'],
                city=validated_data['city'],
                country=validated_data['country'],
                zipcode=validated_data['zipcode']
            )
            retailer.save()
            return retailer

        def update(self, instance, validated_data):
            instance.person_id = validated_data.get('person_id', instance.person_id)
            instance.person_name = validated_data.get('person_name', instance.person_name)
            instance.address = validated_data.get('address', instance.address)
            instance.city=validated_data.get('city',instance.city)
            instance.state = validated_data.get('state', instance.state)
            instance.country = validated_data.get('country', instance.country)
            instance.zipcode = validated_data.get('zipcode', instance.zipcode)
            instance.save()

class DenimSerializer(serializers.ModelSerializer):
    class Meta:
        model=Denim
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'