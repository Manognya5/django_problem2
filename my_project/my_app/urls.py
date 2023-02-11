from django.contrib import admin
from django.urls import path, include
from my_app.views import agent_list

urlpatterns = (
    path('agent/', agent_list),
)