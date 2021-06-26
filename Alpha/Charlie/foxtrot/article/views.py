from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):

    # article = Article(removed=False)
    # article.save()

    article = Article.objects.get(id=1)
    article.delete()

    return HttpResponse('Bingo')