from django.shortcuts import render ,  get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import *
from ujjwal_assignment.models import *

@api_view(['GET' , 'POST' , 'PUT' , 'DELETE'])
def site_list(request):
    if request.method == 'GET':
        students = student.objects.all()
        sites = studentSerializer(students , many = True)
        return Response(sites.data)

    elif request.method == 'POST':
        try:
            students = request.data
            print(students)
            sites = studentSerializer
            sites.create(students)
            return Response("Student data successfully added")
        except Exception as error:
            return Response(str(error))

    elif request.method == 'PUT' :
        pk = request.data.get('student_id') 
        if pk:
            site = student.objects.get(pk=pk)
            print(site , "site")
            sites = studentSerializer()
            print(request.data)
            print(sites.data)
            sites.update(site , request.data)
            return Response("Student data updated")
            print("not valid")
        return Response("error" , status=400)

    elif request.method == 'DELETE':
        print(" In Delete")

        pk = request.data.get('student_id')
        print("Deleted")
        return Response('Student data deleted')





