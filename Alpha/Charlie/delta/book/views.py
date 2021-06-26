from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

# Create your views here.
def index(request):
    # 使用orm添加一条数据到数据库中
    # 创建一个实体类对象，插入数据库中
    # book = Book(name='SpiderMan', author='Peter', price='11')
    # book.save()

    # 查询操作
    # 根据主键查找
    # book = Book.objects.get(id=1)
    # 根据其他字段查找，返回一个列表
    # book2 = Book.objects.filter(name='SpiderMan').first()
    # 获取filter返回的列表中的第一个
    # book2 = book_list.first()
    # print(type(book2))
    # print(book2)
    # print(book)

    # 删除数据
    # book = Book.objects.get(id=1)
    # book.delete()

    # 修改数据
    book = Book.objects.get(id=2)
    book.price = 200
    book.save()


    return HttpResponse('更新数据成功')
