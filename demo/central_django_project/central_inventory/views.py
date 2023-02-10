from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SiteSerializer
from central_inventory.models import *

# Create your views here.

'''def index(request):
    return HttpResponse(
        "This is the view"
    )'''

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def site_list(request):
    if request.method == 'GET':
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        try:
            sites = request.data
            print(sites)
            serializer = SiteSerializer()
            #if serializer.is_valid():
            #print(serializer.data)
            serializer.create(sites)
            #print("is valid", serializer.is_valid())
            #serializer.insert(sites)
            #print("is valid", serializer.is_valid())
            return Response('sites successfully added')
        except Exception as error:
            return Response(str(error))
    
    elif request.method == 'PUT':
        pk = request.data.get('site_id')
        
        print("primary key", pk)
        if pk:
            site = Site.objects.get(pk=pk)
            print(site, "site")
            #serializer = CommentSerializer(comment, data=data)
            serializer = SiteSerializer()
            print(request.data)
            print(serializer.data)
            serializer.update(site, request.data)
            #serializer.save()
            return Response('sites Updated')
            print("not valid")
        return Response("error", status=400)
                
    elif request.method == 'DELETE':
        print("in delete")
        pk = request.data.get('site_id')
        print("deleted")
        site = Site.objects.get(pk=pk).delete()
        print("deleted")
        return Response('sites Deleted')

