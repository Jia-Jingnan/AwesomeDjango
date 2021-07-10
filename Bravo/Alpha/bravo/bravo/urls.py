"""bravo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 首页路由
    url(r'^$', views.home),
    # url第一个参数是正则表达式，只要有一个能够匹配就立即返回，停止往下继续匹配，直接执行对应的视图函数
    # 输入任意url都会默认加/
    # url(r'^test/', views.test), # 如果不加^ ,adfadf/test/这种url也能匹配到test视图函数
    # url(r'^test/$',...)
    # 无名分组就是将括号内的正则表达式匹配到的内容当作位置参数传递给视图函数
    url(r'^test/(\d+)', views.test), # 正则表达式分组
    url(r'^testadd/', views.testadd),

    # 反向解析
    url(r'^func_kkk/', views.func, name='ooo'),

    # w尾页
    url(r'', views.error)
]
