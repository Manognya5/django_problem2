from django.contrib import admin
from django.urls import path
from.views import *
urlpatterns = [
    path('students/',site_list),
]
