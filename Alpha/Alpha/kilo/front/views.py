from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("首页")


def login(request):
    return HttpResponse('登陆页')


def article_detail(request, article_id):
    text = '文章ID:{}'.format(article_id)
    return HttpResponse(text)
