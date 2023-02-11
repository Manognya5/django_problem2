from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RetailerSerializer
from my_app.models import *
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def Retailer_list(request):
    if request.method =='GET':
        retailer_serializer=Retailer.objects.all()
        serializer= RetailerSerializer(retailer_serializer, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        instance=request.data
        serializer=RetailerSerializer(data=instance)
        if serializer.is_valid():
            serializer.save()
            return Response('order successfully added')

    elif request.method=='PUT':
        pk=request.query_params.get('person_id',None)
        if pk:
            retailer_inst=Retailer.objects.get(pk=pk)
            serializer=RetailerSerializer(instance=retailer_inst, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response('order updated')

    elif request.method=='DELETE':
        pk=request.query_params.get('person_id',None)
        retailer_inst=Retailer.objects.get(pk=pk).delete()
        return Response('order deleted')
