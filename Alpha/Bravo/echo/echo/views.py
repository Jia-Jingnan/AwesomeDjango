# Author:   jingnan
# Date:    2021/6/23
# Desc:
from django.shortcuts import render


def index(request):
    context = {
        'persons':[
            '张三',
            '里斯',
            '王武'
        ]
    }
    return render(request, 'index.html', context=context)