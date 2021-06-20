# Author:   jingnan
# Date:    2021/6/20
# Desc:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article),
    path('list/', views.artical_list)
]