from rest_framework import serializers
from .models import *
from django.db.models import fields

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'
        abstraction = True

        def create(self, validated_data):
            agent = Agent (
                agent_id=validated_data['agent_id'],
                agent_name=validated_data['agent_name'],
                agent_phone_number=validated_data['agent_phone_number'],
                agent_city=validated_data['agent_city']
            )
            agent.save()
            return agent

        def update(self, instance, validated_data):
            instance.agent_id = validated_data.get('agent_id', instance.agent_id)
            instance.agent_name = validated_data.get('agent_name', instance.agent_name)
            instance.agent_phone_number = validated_data.get('agent_phone_number', instance.agent_phone_number)
            instance.agent_city = validated_data.get('agent_city', instance.agent_city)
            instance.save()
            return instance

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
