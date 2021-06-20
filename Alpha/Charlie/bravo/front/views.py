from django.shortcuts import render
from django.db import connection


def get_cursor():
    return connection.cursor()


# Create your views here.
# 视图函数
def index(request):
    cursor = get_cursor()
    cursor.execute('select id, name, author from book')
    books = cursor.fetchall()  # 返回的是一个列表
    # 准备上下文
    context = {
        'books': books
    }
    return render(request, 'index.html', context=context)


def add_book(request):
    pass


def book_detail(request, book_id):
    pass
