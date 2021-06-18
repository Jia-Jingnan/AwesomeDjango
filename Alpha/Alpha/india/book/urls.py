# coding=UTF-8
from django.urls import path
from . import views


urlpatterns = [

    path('', views.book),
    path('detail/<book_id>', views.book_detail)
]