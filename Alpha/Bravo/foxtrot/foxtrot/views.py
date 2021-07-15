# Author:   jingnan
# Date:    2021/7/15
# Desc:
from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    next = request.GET.get('next')
    text = '登陆完成后要跳转的页面URL是%s' % next
    return HttpResponse(text)

def index(request):
    return render(request, 'index.html')


def book(request):
    return HttpResponse('读书页面')


def movie(request):
    return HttpResponse('电影页面')


def city(request):
    return HttpResponse('同城页面')


def book_detail(request, book_id, category):
    text = '图书ID：%s, 分类是%s'% (book_id, category)
    return HttpResponse(text)