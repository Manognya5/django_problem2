from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):  # site
    class Meta:
        model = Product
        fields = "__all__"

        def create(self, validated_data):
            prod = Product(
                product_id=validated_data["product_id"],
                product_name=validated_data["name"],
                store_id=validated_data["store_id"],
            )
            prod.save()
            return prod

        def update(self, instance, validated_data):
            instance.product_id = validated_data.get("product_id", instance.product_id)
            instance.product_name = validated_data.get("name", instance.product_name)
            instance.store_id = validated_data.get("store_id", instance.store_id)
            instance.save()
            return instance


class CustomerSerializer(serializers.ModelSerializer):  # iap
    class Meta:
        model = Customer
        fields = "__all__"

        def create(self, validated_data):
            cust = Customer(
                cust_id=validated_data["cust_id"],
                cust_name=validated_data["name"],
                product_id=validated_data["product_id"],
                quantity=validated_data["quantity"],
                total=validated_data["total"],
            )
            cust.save()
            return cust

        def update(self, instance, validated_data):
            instance.cust_id = validated_data.get("cust_id", instance.cust_id)
            instance.cust_name = validated_data.get("name", instance.cust_name)
            instance.product_id = validated_data.get("product_id", instance.product_id)
            instance.quantity = validated_data.get("quantity", instance.quantity)
            instance.total = validated_data.get("total", instance.total)
            instance.save()
            return instance


class StoreSerializer(serializers.ModelSerializer):  # switch
    class Meta:
        model = Store
        fields = "__all__"

        def create(self, validated_data):
            store = Store(
                store_id=validated_data["store_id"],
                store_name=validated_data["name"],
                city=validated_data["city"],
                state=validated_data["state"],
                country=validated_data["country"],
                zipcode=validated_data["zipcode"],
            )
            store.save()
            return store

        def update(self, instance, validated_data):
            instance.store_id = validated_data.get("store_id", instance.store_id)
            instance.store_name = validated_data.get("name", instance.store_name)
            instance.city = validated_data.get("city", instance.city)
            instance.state = validated_data.get("state", instance.state)
            instance.country = validated_data.get("country", instance.country)
            instance.zipcode = validated_data.get("zipcode", instance.zipcode)
            instance.save()
            return instance
