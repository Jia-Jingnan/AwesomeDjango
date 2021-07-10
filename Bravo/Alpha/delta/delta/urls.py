"""delta URL Configuration

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
    # url(r'^login/', views.MyLogin.as_view()),
    # 上述代码在django启动时会立即执行as_view方法，会变成
    # url(r'^login/', views.view)  与FBV一模一样
    # CBV 与FBV在路由被指上是一样的，都是路由对应函数内存地址
    url(r'^index/', views.index),
    # 模板的继承
    url(r'^home/', views.home),
    url(r'^login/', views.login),
    url(r'^reg/', views.reg),
]
