from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StoreSerializer, ProductSerializer, CustomerSerializer
from product_inventory.models import *

# Create your views here.

"""def index(request):
    return HttpResponse(
        "This is the view"
    )"""


@api_view(["GET", "POST", "PUT", "DELETE"])
def store_list(request):
    if request.method == "GET":
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        try:
            store = request.data
            print(store)
            serializer = StoreSerializer()
            serializer.create(store)
            return Response("store successfully added")
        except Exception as error:
            return Response(str(error))

    elif request.method == "PUT":
        pk = request.data.get("store_id")
        print("primary key", pk)
        if pk:
            store = Store.objects.get(pk=pk)
            print(store, "store")
            serializer = StoreSerializer()
            print(request.data)
            print(serializer.data)
            serializer.update(store, request.data)
            return Response("stores Updated")
            print("not valid")
        return Response("error", status=400)

    elif request.method == "DELETE":
        print("in delete")
        pk = request.data.get("store_id")
        print("deleted")
        store = Store.objects.get(pk=pk).delete()
        print("deleted")
        return Response("store Deleted")


@api_view(["GET", "POST", "PUT", "DELETE"])
def product_list(request):
    if request.method == "GET":
        prod = Product.objects.all()
        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        try:
            prod = request.data
            print(prod)
            serializer = ProductSerializer()
            serializer.create(prod)
            return Response("product successfully added")
        except Exception as error:
            return Response(str(error))

    elif request.method == "PUT":
        pk = request.data.get("product_id")
        print("primary key", pk)
        if pk:
            prod = Product.objects.get(pk=pk)
            print(prod, "product")
            serializer = ProductSerializer()
            print(request.data)
            print(serializer.data)
            serializer.update(prod, request.data)
            return Response("products Updated")
            print("not valid")
        return Response("error", status=400)

    elif request.method == "DELETE":
        print("in delete")
        pk = request.data.get("product_id")
        print("deleted")
        prod = Product.objects.get(pk=pk).delete()
        print("deleted")
        return Response("Product Deleted")


@api_view(["GET", "POST", "PUT", "DELETE"])
def customer_list(request):
    if request.method == "GET":
        cust = Customer.objects.all()
        serializer = CustomerSerializer(cust, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        try:
            cust = request.data
            print(cust)
            serializer = CustomerSerializer()
            serializer.create(cust)
            return Response("customer successfully added")
        except Exception as error:
            return Response(str(error))

    elif request.method == "PUT":
        pk = request.data.get("cust_id")
        print("primary key", pk)
        if pk:
            cust = Customer.objects.get(pk=pk)
            print(cust, "customer")
            serializer = CustomerSerializer()
            print(request.data)
            print(serializer.data)
            serializer.update(cust, request.data)
            return Response("customer Updated")
            print("not valid")
        return Response("error", status=400)

    elif request.method == "DELETE":
        print("in delete")
        pk = request.data.get("cust_id")
        print("deleted")
        cust = Product.objects.get(pk=pk).delete()
        print("deleted")
        return Response("Customer Deleted")
