# Author:   jingnan
# Date:    2021/6/20
# Desc:
from django.shortcuts import render


# 定一个模型
class Person():

    def __init__(self, name):
        self.name = name


def index(request):

    # p = Person('alpha')
    # context = {
    #     'person': p
    # }

    # context用来存储上下文参数，既可以在html中展示的变量都可以在context中定义
    # context为字典类型
    # context = {
    #     'username': 'bravo'
    # }

    # p是一个字典类型
    # context = {
    #     'p': {'person': 'charlie'}
    # }

    # p 是一个列表
    context = {
        'p': [
            "Tony Stark",
            "Peter Park",
            "Thor",
            "Stranger",
            "Loki"
        ]
    }
    return render(request, 'index.html', context=context)