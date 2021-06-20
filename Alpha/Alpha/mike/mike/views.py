# Author:   jingnan
# Date:    2021/6/20
# Desc:

from django.http import HttpResponse


book_list = [
    '三国演义',
    '水浒传',
    '西游记',
    '烘炉梦'
]


def books(request, page=0):
    return HttpResponse(book_list[page])