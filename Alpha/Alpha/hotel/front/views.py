from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('front首页')


def login(request):
    return HttpResponse('front登陆首页')

