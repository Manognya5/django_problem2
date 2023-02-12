from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('books/',book_list ),
    path('authors/' , authors_list),
]