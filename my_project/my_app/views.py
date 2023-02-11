from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serializers import AgentSerializer
from my_app.models import *

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def agent_list(request):

    if request.method == 'GET':
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        agents = request.data
        serializer = AgentSerializer(data=agents)
        if serializer.is_valid():
            serializer.save()
            return Response('Agents successfully added')

    elif request.method =='PUT':
        pk = request.query_params.get('agent_id', None)
        if pk:
            agents = Agent.objects.get(pk=pk)
            serializer = AgentSerializer(instance=agents, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response('Agents Updated')
                
    elif request.method == 'DELETE':
        pk = request.query_params.get('agent_id', None)
        agent_inst = Agent.objects.get(pk=pk).delete()
        return Response('Agents Deleted')