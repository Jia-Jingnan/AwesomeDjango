from django.http import HttpResponse
from django.shortcuts import reverse, redirect


# Create your views here.
def index(request):
    # 首页传入username时需要登陆
    username = request.GET.get('username')
    if username:
        return HttpResponse("首页")
    else:
        return redirect(reverse('login'))



def login(request):
    return HttpResponse('登陆页')


def article_detail(request, article_id):
    text = '文章ID:{}'.format(article_id)
    return HttpResponse(text)
