# Author:   jingnan
# Date:    2021/6/20
# Desc:
from django.shortcuts import render


def index(request):
    # context用来存储上下文参数，既可以在html中展示的变量都可以在context中定义
    # context为字典类型
    context = {
        'username': 'bravo'
    }
    return render(request, 'index.html', context=context)