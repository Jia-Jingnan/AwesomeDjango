from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^reg/', views.reg),
    url(r'^index/', views.index),
    # 返回json字符串
    url(r'^ab_json/', views.ab_json),
    # 上传文件
    url(r'ab_file/', views.ab_file),

    # CBV路由
    url(r'^login/', views.MyLogin.as_view())



]
