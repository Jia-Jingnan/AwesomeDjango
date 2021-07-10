from django.conf.urls import url
from django.contrib import admin
from app02 import views

urlpatterns = [
    url(r'^reg/', views.reg),


]
