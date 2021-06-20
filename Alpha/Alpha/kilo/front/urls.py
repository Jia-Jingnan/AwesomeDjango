# Author:   jingnan
# Date:    2021/6/20
# Desc:

from django.urls import path
from . import views


urlpatterns = [

    path('', views.index),
    path('login/', views.login),
    path('detail/<int:article_id>/', views.article_detail)
]