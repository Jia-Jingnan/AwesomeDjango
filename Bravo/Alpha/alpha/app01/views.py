from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from app01 import models


# HttpResponse 返回字符串
def index(request):
    '''
    :param request: 请求相关的所有数据对象
    :return:
    '''
    # return HttpResponse('App01 Index')
    # return render(request, 'index.html')
    return redirect('/home/')

def home(request):
    return HttpResponse('home')


def login(request):
    # 返回一个登录界面

    '''
    get请求和post请求的处理代码是不一样的
    如何判断当前请求是get请求还是post请求
    '''

    print(request)
    # 获取当前请求的请求方式
    # print(request.method,type(request.method))
    # if request.method == 'GET':
    #     print('来了，老弟')
    # elif request.method == 'POST':
    #     return HttpResponse('收到')
    # return render(request, 'login.html')

    # 简写
    if request.method == 'POST':
        # 获取用户提交的数据
        print(request.POST) # 获取用户提交的post数据，不包含文件
        # <QueryDict: {'username': ['adfa'], 'password': ['adfa']}>
        # get只会获取列表最后一个元素
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, type(username))
        # 获取全部元素,使用getList方法
        # hobby = request.POST.getlist('hobby')
        # print(hobby, type(hobby))

        # 查询数据

        # fileter相当于where
        res = models.User.objects.filter(username=username)
        # <QuerySet [<User: User object>]> 列表嵌套数据对象
        # [数据对象1， 数据对象2， 数据对象3]
        # QuerySet不支持负数索引，不推荐使用索引方式取值
        # print(len(res))
        # print(res[0].username)
        # print('对象：', res[0])
        # user = res[0],# 不推荐使用索引取值
        # 推荐使用first()方法
        print(res)
        user = res.first()
        print(type(password))
        print(type(user.password))
        # 打印对象属性
        # print(user.username)
        # 校验数据
        if user:
            if int(password) == user.password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户不存在')
    # 获取url后面携带的参数，获取get请求数据
    # print(request.GET)
    # print(request.GET.get('hobby'))
    # print(request.GET.getlist('hobby'))
    return render(request,'login.html')


def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 校验是否在数据库中已存在（忽略），再插入数据库
        # res = models.User.objects.create(username=username, password=password, age=10)
        # 打印创建的对象
        # print(res)
        # 第二种插入方式
        user = models.User(username=username, password=password, age=10)
        user.save()
    # 先给用户返回一个注册页面
    return render(request, 'register.html')


# 现将所有数据展现在前端，然后增加两个按钮，编辑和删除

def list(request):
    # 查询出user表里面所有的数据
    # 方式1
    # user_queryset = models.User.objects.filter()
    # 方式2， 获取所有的数据
    user_queryset = models.User.objects.all()
    print(user_queryset)


    # locals表示将list函数内的所有变量都传递给HTML页面
    return render(request, 'list.html', locals())


def edit(request):
    # 点击编辑按钮，后端发送要编辑的用户的ID,使用？user_id=1的方式
    # http://127.0.0.1:8000/edit/?user_id=1  ?user_id=1不参与路径匹配
    # 获取传入的user_id
    user_id = request.GET.get('user_id')
    print('传入的user_id:', user_id)
    # 要被编辑的对象
    edit_obj = models.User.objects.filter(id=user_id).first()

    if request.method == 'POST':
        # 获取编辑后的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('编辑后的username:', username)
        print('编辑后的password', password)

        # 数据库中修改对应的数据内容
        # 修改数据方式1, 批量更新
        # models.User.objects.filter(id=user_id).update(username=username, password=password)
        # 修改数据方式2, 针对一个对象单独更新
        edit_obj.username = username
        edit_obj.password = password
        edit_obj.save()
        """
        上述方法在字段比较多的时候更新效率低
        从头到尾将数据的所有字段全部更新一遍，无论该该字段信息是否改变
        """

        # 跳转到数据展示页面
        return redirect('/list/')


    # 查询该用户
    user = models.User.objects.filter(id=user_id).first()

    return render(request, 'edit.html', locals())


def delete(request):
    # 获取想要删除的Id
    delete_id = request.GET.get('user_id')
    # 删除数据
    models.User.objects.filter(id=delete_id).delete()

    return redirect('/list/')