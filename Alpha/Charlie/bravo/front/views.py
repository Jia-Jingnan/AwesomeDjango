from django.shortcuts import render, redirect, reverse
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
    if request.method == 'GET':
        return render(request, 'add_book.html')
    else:
        name = request.POST.get('name')
        author = request.POST.get('author')
        cursor = get_cursor()
        cursor.execute("insert into book(id, name, author) values (null, '%s', '%s')" % (name, author))
        return redirect(reverse('index'))


def book_detail(request, book_id):
    cursor = get_cursor()
    cursor.execute("select id, name, author from book where id = %s" % book_id)
    book = cursor.fetchone()
    context = {'book': book}
    return render(request, 'book_detail.html', context)


def delete_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        cursor = get_cursor()
        cursor.execute("delete from book where id = %s" % book_id)
        return redirect(reverse('index'))
    else:
        raise RuntimeError('删除图书的方法错误')
