# Author:   jingnan
# Date:    2021/6/20
# Desc:

from django.shortcuts import render
from django.db import connection


def index(request):

    # 获取游标
    cursor = connection.cursor()
    # cursor.execute("insert into book(id, name, author) values (null, '西游记','吴承恩')")
    cursor.execute("select id, name, author from book")
    rows = cursor.fetchall()  # 返回全部数据
    for row in rows:
        print(row)
    return render(request, 'index.html')