# coding=UTF-8
from django.urls import path
from . import views

# app_name
# app_name = 'book'

urlpatterns = [

    path('', views.book),
    path('detail/<book_id>', views.book_detail)
]