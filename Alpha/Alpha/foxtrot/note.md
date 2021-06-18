URL 传参：  
1.采用再url使用变量的方式，再path的第一个参数中，使用<参数名>的方式传递参数
然后在视图函数中也要写一个在参数，视图函数中的参数与path中的参数名称保持一致，url中
可以传递多个参数  
2.查询字符串的方式，在url中，不需要单独匹配查询字符串的部分，只需要在视图函数中使用
request.GET.get('参数名称')方式获取
```python
def author_detial(request):
    # request包含客户端或者浏览器请求的所有的数据,获取GET请求中id的值
    author_id = request.GET.get("id")
    text = 'author_id是%s' % author_id
    return HttpResponse(text)
```
因为查询字符串采用的是GET请求，所以通过request.GET来获取参数，并且因为GET类似一个字典的数据类型
所以获取值的方式与字典是一样的