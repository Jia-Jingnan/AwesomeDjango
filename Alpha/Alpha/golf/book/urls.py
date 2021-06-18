# coding=UTF-8
from django.urls import path
from . import views

urlpatterns = [

    # book/
    path('', views.book),
    # book/detail/1
    path('detail/<book_id>', views.book_detail),
    path('list/', views.book_list),
]