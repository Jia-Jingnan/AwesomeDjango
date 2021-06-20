from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def article(request):
    return HttpResponse('文章首页')


def article_list(request, categories):
    print(reverse('list',kwargs={'categories':categories}))
    return HttpResponse('文章分类为{}'.format(categories))


def article_detail(request, article_id):
    print(type(article_id))
    return HttpResponse('文章ID为{},类型为{}'.format(article_id, type(article_id)))