from django.shortcuts import render, reverse
from django.http import HttpResponse


# Create your views here.
def home(request):
    # 后端方向解析
    print(reverse('ooo'))
    return render(request, 'home.html')


def test(request,xx):
    print(xx)
    return HttpResponse('test')


def func(request):
    return HttpResponse('FUNCSSSSSSSSSSSSSSSSSSSSSSSS')


def error(request):
    return HttpResponse('404')


def testadd(request):
    return HttpResponse('testadd')