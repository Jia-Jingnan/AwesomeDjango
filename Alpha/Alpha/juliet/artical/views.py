from django.http import HttpResponse


# Create your views here.
def article(request):
    return HttpResponse('文章首页')


def artical_list(request):
    return HttpResponse('文章列表')