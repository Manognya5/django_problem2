from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SiteSerializer
from central_inventory.models import *


@api_view(['GET','POST','PUT','DELETE'])
def site_list(request):
    if request.method == 'GET':
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            sites = request.data
            serializer = SiteSerializer()
            serializer.create(sites)
            return Response('sites successfully added')
        except Exception as error:
            return Response(str(error))
        # if serializer.is_valid():
        #     serializer.create(request.data)
        #     return Response('sites successfully added')
            
    elif request.method == 'PUT':
        pk = request.data.get('site_id')
        if pk:
            site = Site.objects.get(pk=pk)
            serializer = SiteSerializer(instance=site, data=request.data)
            if serializer.is_valid():
                serializer.update(instance=site, valid_data=request.data)
                #serializer.save()
                return Response('sites Updated')
            return Response("error", status=400)

    elif request.method == 'DELETE':
        pk = request.query_params.get('site_id', None)
        site = Site.objects.get(pk=pk).delete()
        return Response('sites Deleted')

# Create your views here.

def index(request):
    return HttpResponse("This is the view")
