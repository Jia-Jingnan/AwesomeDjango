# Author:   jingnan
# Date:    2021/6/20
# Desc:
from django.shortcuts import render


def index(request):

    # 上下文
    # context = {
    #     'age': 20
    # }
    context = {
        'heros':[
            'IronMan',
            'SpiderMan',
            'Captain American',
            "Doctor Stranger",
            "God of Thunder"
        ]
    }
    return render(request, 'index.html', context=context)