from django.http import HttpResponse
from django.shortcuts import reverse, redirect


# Create your views here.
def index(request):
    # 首页传入username时需要登陆
    username = request.GET.get('username')
    if username:
        return HttpResponse("首页")
    else:
        # reverse不需要传参的url地址 login/
        # return redirect(reverse('login'))
        # reverse需要传参数的url地址  detial/1
        # return redirect(reverse('artical', kwargs={'article_id': 1}))
        # reverse需要传查询字符串的URL地址，detail?artical_id=11
        return redirect(reverse('login') + '?next=/')



def login(request):
    return HttpResponse('登陆页')


def article_detail(request, article_id):
    text = '文章ID:{}'.format(article_id)
    return HttpResponse(text)
