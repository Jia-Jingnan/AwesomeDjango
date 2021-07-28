# Author:   jingnan
# Date:    2021/7/29
# Desc:
from django.shortcuts import render


def greet():
    return 'hello'


def index(request):
    context = {
        'greet': greet
    }
    return render(request, 'index.html', context=context)


def add_view(request):
    context = {
        'value1': ['1','2','3'],
        'value2': ['1','2','3']
    }
    return render(request, 'add.html', context)


def cut_view(request):
    return render(request, 'cut.html')