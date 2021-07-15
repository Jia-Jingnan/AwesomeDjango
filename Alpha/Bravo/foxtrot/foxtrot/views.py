# Author:   jingnan
# Date:    2021/7/15
# Desc:
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def book(request):
    return HttpResponse('读书页面')


def movie(request):
    return HttpResponse('电影页面')


def city(request):
    return HttpResponse('同城页面')