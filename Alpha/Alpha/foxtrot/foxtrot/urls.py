"""foxtrot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views
from django.http import HttpResponse
# 内置的转换器
from django.urls import converters


def index(request):
    return HttpResponse('首页')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('book/', views.book),
    path('book/detail/<book_id>/<category_id>', views.book_detail),
    # 查询字符串方式传参,即通过？传参
    path('book/author/', views.author_detial),
    # 指定int类型传参,或者指定字符串(除了/之外)
    path('book/publish/<str:publish_id>', views.pulish_detail),
]
