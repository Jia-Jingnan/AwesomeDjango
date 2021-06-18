from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('CMS首页')


def login(request):
    return HttpResponse('CMS登陆首页')
