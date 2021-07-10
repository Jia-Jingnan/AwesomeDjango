"""charlie URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from app01 import urls as app01_urls
from app02 import urls as app02_urls
from app01 import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 首页
    url(r'^$', views.home),
    # # 无名分组反向解析
    # url(r'^index/(\d+)/', views.index, name='xxx'),
    # # 有名分组的反向解析
    # url(r'^func/(?P<year>\d+)/', views.func, name='ooo')
    # app01的路由
    url(r'^app01/', include('app01.urls', namespace='app01')),
    url(r'^app02/', include('app02.urls', namespace='app02')),
    # 路由分发方式2 ，使用别名
    # url(r'^app01/', include(app01_urls))
    # 将第二个路由里面的内容先转成整形然后再以关键字参数传递给后面的视图函数
    # path('index/<int:id>', views.index)

]


'''
无名分组反向解析
url(r'^index/(\d+)/', views.index, name='xxx'),

# 前端
{% url 'xxx' 123 %}
{% url 'xxx' user.id %}

# 后端
reverse('xxx', args=(1,))
reverse('xxx', args=(edit_id,))

这个数字在写代码的时候应该放什么
数字一般情况下放的是数据的主键，来做数据的编辑和删除
'''