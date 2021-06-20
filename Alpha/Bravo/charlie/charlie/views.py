# Author:   jingnan
# Date:    2021/6/20
# Desc:
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')