# Author:   jingnan
# Date:    2021/6/20
# Desc:

from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('detail/<int:article_id>/', views.article_detail, name='artical')
]