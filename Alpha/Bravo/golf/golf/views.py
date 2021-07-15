# Author:   jingnan
# Date:    2021/7/15
# Desc:
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'info': '<a href="www.baidu.com">百度</a>'
    }
    return render(request, 'index.html', context)