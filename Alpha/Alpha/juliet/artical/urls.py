# Author:   jingnan
# Date:    2021/6/20
# Desc:
from django.urls import re_path
from . import views

urlpatterns = [
    # python中正则表达式，r代表原生字符串，未经过任何处理。
    # ^表示以..为开头
    # $表示以..为结尾
    # r'^$' 表示一个空字符串
    re_path(r'^$', views.article),
    # artical/list/<year>
    # r^list/ 表示以list/开头， /$表示以/结尾
    # 表达式中()括号表示要捕获的值
    # ?P 是 named group，定一个一个变量
    # ?P<year>表示定义一个变量名year，\d表示0-9的数字，{4}表示有4个数字
    re_path(r'^list/(?P<year>\d{4})/$', views.artical_list),
    re_path(r'^list/(?P<year>\d{4})/(?P<month>\d{2})/$', views.artical_list),
]