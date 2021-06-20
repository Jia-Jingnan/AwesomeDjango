from django.http import HttpResponse


# Create your views here.
def article(request):
    return HttpResponse('文章首页')


def artical_list(request, year, month):
    return HttpResponse('{}年{}月文章列表'.format(year, month))