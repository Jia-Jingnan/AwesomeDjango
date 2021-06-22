# Author:   jingnan
# Date:    2021/6/23
# Desc:

from django.shortcuts import render


def index(request):
    context = {
        'books':[
            {
                'name': '三国演绎',
                'author': '罗贯中',
                'price': '199'
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': '109'
            },
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': '109'
            },
        ],
        'person':{
            'username': 'zhiliao',
            'age': '18',
            'height': 180
        }
    }
    return render(request, 'index.html',context=context)