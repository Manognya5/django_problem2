from rest_framework import serializers, response
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields =['book_id' , 'name' , 'yop' , 'publisher' , 'author_id']
        
        #update function
        def create(self , validated_data):
            book1 = book(
                book_id = validated_data['book_id'],
                name = validated_data['name'],
                yop = validated_data['yop'],
                publisher = validated_data['publisher'],
                author_id = validated_data['author_id']
                )
            book1.save()
            return book1
        
        def update(self , instance , validated_data):
            instance.book_id = validated_data.get('book_id' , instance.book_id)
            instance.name = validated_data.get('book_name' , instance.book_name)
            instance.yop = validated_data.get('yop' , instance.yop)
            instance.publisher = validated_data.get('publisher' , instance.publisher)
            instance.author_id  = validated_data.get('author_id' , instance.author_id)
            instance.save()
            return instance




    

class AuthorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = author
        fields = ['auth_id' , 'auth_name' , 'place' , 'nationality' , 'yob']


        def create(self , validated_data):
            auth = author(
                auth_id = validated_data['auth_id'],
                auth_name = validated_data['auth_name'],
                place = validated_data['place'],
                nationality = validated_data['nationality'],
                yob = validated_data['yob']
            )
            auth.save()
            return auth
        
        def update(self , instance , validated_data):
            instance.auth_id  = validated_data.get('auth_id' , instance.auth_id )
            instance.auth_name = validated_data.get('auth_name' , instance.auth_name )
            instance.place = validated_data.get('place' , instance.place )
            instance.nationality = validated_data.get('nationality' , instance.nationality )
            instance.yob = validated_data.get('yob' , instance.yob )
            instance.save()
            return instance






    

