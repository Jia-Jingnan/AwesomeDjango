from django.http import HttpResponse


# Create your views here.
def book(request):
    return HttpResponse("图书首页")


def book_detail(request, book_id, category_id):
    # 可以从数据库中根据book_id查询到图书信息
    text = "您获取的book_id为%s,图书分类是%s"%(book_id, category_id)
    return HttpResponse(text)


def author_detial(request):
    # request包含客户端或者浏览器请求的所有的数据,获取GET请求中id的值
    author_id = request.GET.get("id")
    text = 'author_id是%s' % author_id
    return HttpResponse(text)


def pulish_detail(request, publish_id):
    text = '出版社的id为%s' % publish_id
    return HttpResponse(text)

