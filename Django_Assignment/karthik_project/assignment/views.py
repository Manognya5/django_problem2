from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DetailsSerializer
from assignment.models import *

# def index(request):
#     return HttpResponse("Here I am at views")

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = Details.objects.all()
        serializer = DetailsSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        users = request.data
        serializer = DetailsSerializer(data=users)
        if serializer.is_valid():
            #serializer.save()
            serializer.create(request.data)
            return Response('Users successfully added')
        else:
            return Response("Invalid Input")
    elif request.method == 'PUT':
        primary = request.query_params.get('user_id', None)
        if primary:
            site = Details.objects.get(pk=primary)
            serializer = DetailsSerializer(instance=site, data=request.data)
            if serializer.is_valid():
                #serializer.save()
                serializer.update(site,request.data)
                return Response('Users Updated')
        else:
            return Response("Invalid Input")
    elif request.method == 'DELETE':
        pk = request.query_params.get('user_id', None)
        site = Details.objects.get(pk=pk).delete()
        return Response('Users Deleted')