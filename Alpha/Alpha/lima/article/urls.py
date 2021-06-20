# Author:   jingnan
# Date:    2021/6/20
# Desc:
from django.urls import re_path, path, converters, register_converter
from . import views

urlpatterns=[
    path('', views.article),
    # \w 包含 0-9 a-z，A-Z
    # re_path(r'list/(?P<categories>\w+|(\w+\+\w+)+)/',views.article_list),
    # 使用自定义转换器 cate
    path("list/<cate:categories>/",views.article_list,name='list'),
    path('detail/<int:article_id>/', views.article_detail),
]