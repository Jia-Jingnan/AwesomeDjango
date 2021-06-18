from django.http import HttpResponse
from django.shortcuts import redirect


# Create your views here.
def index(request):
    # ?username=xxx，如果没有传usename就自动跳转到front登陆页面
    username = request.GET.get('username')
    if username:
        return HttpResponse('front首页')
    else:
        return redirect("/login/")


def login(request):
    return HttpResponse('front登陆首页')

