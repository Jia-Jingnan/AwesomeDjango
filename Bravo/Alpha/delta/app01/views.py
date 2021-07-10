from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.
class MyLogin(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return HttpResponse('Welcome Post')


def index(request):
    # 模板语法可以传递的后端数据类型
    n = 1
    f = 11.0
    b = True
    s = 'hello'
    l = ['Tony', 'Peter', 'Thor']
    t = ('111', '222', '333')
    d = {'username': 'Thor', 'age': '1800', 'hobby': [11,22,33,{'info': 'NB'}]}
    se = {'晶晶', '盈盈'}
    # 函数
    def func():
        print('我被执行了')
        return '另一半在等你'

    # 类
    class MyClass(object):
        def get_self(self):
            return 'self'

        @staticmethod
        def get_func():
            return 'func'

        @classmethod
        def get_class(cls):
            return 'cls'

        # 对象被展示到HTML页面，就类似于执行了打印操作也会触发__str__
        def __str__(self):
            return '到底会不会'

    obj = MyClass()

    file_size = 1222
    import datetime

    current_time = datetime.datetime.now()


    # 文章摘要
    info = 'WEFAFASFDHJKSHAJSDSAJKHDKJSBDFHASFJEKAGWEFKJSJADFJAGEFJJAWEFBJAEW'

    # 切取单词
    eng = 'I am Thor, God of Tunder'

    return render(request, 'index.html', locals())

    msg = 'I am Loki, God of mischief'

    hhh = '<h1>敏敏</h1>'

    sss = '<script>alert(1)</script>'
    # 转义
    from django.utils.safestring import mark_safe
    ssss = '<script>alert(1)</script>'
    mark_safe(ssss)

'''
模板语法相关
{{}}变量相关
{%%}逻辑相关
'''

# 自定义过滤器，标签，inclusion_tag，三步走
# 1.在应用下创建一个名字必须叫templatetags文件夹
# 2.在该文件夹内创建任意名的py文件，如：mytag.py
# 3.在该py文件下必须先书写下面两句话
# from django import template
# register = template.Library()

# 自定义inclusion_tag
# 先定义一个方法，在页面上调用该方法，并且可以传值
# 该方法会生成一些数据，然后传递给一个html页

def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def reg(request):
    return render(request, 'reg.html')