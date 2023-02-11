from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("store/", store_list),
    path("product/", product_list),
    path("customer/", customer_list),
]
