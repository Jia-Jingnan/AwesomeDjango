# Author:   jingnan
# Date:    2021/6/23
# Desc:

from django.shortcuts import render


def index(request):
    context = {
        'books':[
            'SpriderMan',
            'IronMan',
            'Doctor Stranger',
            'Thor',
            'Captain American'
        ],
        'person':{
            'username': 'zhiliao',
            'age': '18',
            'height': 180
        }
    }
    return render(request, 'index.html',context=context)