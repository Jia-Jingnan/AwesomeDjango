# coding=UTF-8
from django.urls import path
from . import views

# 定义命名空间
app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login')
]