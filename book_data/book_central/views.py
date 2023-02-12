from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializer import *
from book_central.models import *



@api_view(['GET' , 'POST' , 'PUT' , 'DELETE'])
def book_list(request):
    if request.method == 'GET':
        books = book.objects.all()
        sites = BookSerializer(books , many = True)
        return Response(sites.data)
    
    elif request.method == 'POST':
        sites = request.data
        serializer = BookSerializer(data=sites)
        if serializer.is_valid():
            serializer.update(sites)
            return Response('sites successfully added')
        else:
            return Response('Invalid input')
        
    elif request.method == 'PUT':
        #primary = request.query_params.get('book_id' , None)
        pk = request.data.get('book_id')
        if pk:
            book1 = book.objects.get(pk=pk)
            serializer = BookSerializer(instance=book1 , data = request.data)
            if serializer.is_valid():
                serializer.update(book1, request.data)
                #serializer.update(book1 , request.data)
                return Response('Updated successfully')
            else:
                return Response('error in PUT ')
        else:
            return Response('invalid input')
        
    elif request.method == 'DELETE':
        # pk = request.query_params.get('book_id' , None)
        # book = book.objects.get(pk=pk).delete()
        return Response('Books deleted')


        
@api_view(['GET' , 'PUT' , 'POST' , 'PATCH'])
def authors_list(request):
    if request.method == 'GET':
        authors = author.objects.all()
        auths = AuthorSerialiser(authors , many = True)
        return Response(auths.data)
    elif request.method == 'POST':
        auth = request.data
        serializer = AuthorSerialiser(data=auth)
        if serializer.is_valid():
            serializer.create(auth)
            return Response("POST happened successfully")
        else:
            return Response("Error in post")
        
    elif request.method == 'PUT':
        pk = request.data.get('author_id')
        if pk:
            author1 = author.object.get(pl=pk)
            serializer = AuthorSerialiser(instance=author1 , data = request.data)
            if serializer.is_valid():
                serializer.update()

            else:
                return response("Error in PUT")




    



# def index(request):
#     return HttpResponse("This is the view")


# Create your views here.


# Create your views here.
