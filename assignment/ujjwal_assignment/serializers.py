from rest_framework import serializers
from .models import *


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"

    def create(self, validated_data):
        site = student (
            site_id = validated_data['student_id'],
            site_first_name = validated_data['student_first_name'],
            site_last_name = validated_data['student_last_name'],
            site_address = validated_data['student_address'],
            site_city = validated_data['student_city'],
            site_state = validated_data['student_state'],
            site_country = validated_data['student_country'],
        )
        site.save()
        return site


    def update(self, instance, valid_data):
        instance.student_id = valid_data.get('student_id' , instance.student_id)
        instance.student_first_name = valid_data.get('student_first_name' , instance.student_first_name)
        instance.student_last_name = valid_data.get('student_last_name' , instance.student_last_name)
        instance.student_address = valid_data.get('student_address' , instance.student_address)
        instance.student_city = valid_data.get('student_city' , instance.student_city)
        instance.student_state= valid_data.get('student_state' , instance.student_state)
        instance.student_country = valid_data.get('student_country' , instance.student_country)
        instance.save()
        return instance

        
        #return super().update(instance, validated_data)

class lecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = lecturer
        fields = "__all__"

class class_roomSerializer(serializers.ModelSerializer):
    class Meta:
        model = class_room
        fields = "__all__"