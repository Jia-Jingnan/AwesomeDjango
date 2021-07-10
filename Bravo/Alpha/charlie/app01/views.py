from django.shortcuts import render, reverse
from django.http import HttpResponse


# Create your views here.
# 视图函数必须返回一个httpResponse对象
def index(request):
    # return HttpResponse('index')
    # return render(request, 'home.html')
    from django.template import Template, Context
    res = Template('<h1>{{ user }}</h1>')
    con = Context({'user': {'username': 'thor', 'password':'123'}})
    ret = res.render(con)
    print(ret)
    return HttpResponse(ret)


def home(request):
    # 后端反向解析
    print(reverse('xxx',args=(1,)))
    # 有名分组反向解析, 写法1
    print(reverse('ooo', kwargs={'year': 123}))
    # 写法2
    print(reverse('ooo', args=(111,)))
    return render(request, 'home.html')


def func(request, year):
    return HttpResponse('func')


def reg(request):
    return HttpResponse('app01 reg')

# import json
from django.http import JsonResponse
def ab_json(request):
    # user_dict = {'username': 'thor 好厉害，好礼哈', 'password': '123', 'hobby': 'fight'}
    # 先转成json格式字符串
    # json_str = json.dumps(user_dict,ensure_ascii=False)
    # 将该字符串返回
    # return JsonResponse(user_dict, json_dumps_params={'ensure_ascii': False})

    # 列表序列化
    l = [1,2,4,5,6]
    return JsonResponse(l, safe=False)


def ab_file(request):
    if request.method == 'POST':
        # request.POST只能获取键值对数据
        # print(request.POST)
        # 获取文件数据
        print(request.FILES)
        file_obj = request.FILES.get('file')
        print(file_obj.name)
        with open(file_obj.name, 'wb') as f:
            for line in file_obj.chunks():
                f.write(line)

        print(request.path)
        print(request.get_full_path())
    return render(request, 'form.html')



# 类试图
# CBV的特点，能够根据请求方式的不同直接匹配到对应的方法执行
from django.views import View

class MyLogin(View):
    # get请求时走的逻辑
    def get(self, request):
        return render(request,'form.html')

    # post请求时走的逻辑
    def post(self, request):
        return HttpResponse('Pos方法')