from django.http import HttpResponse


# Create your views here.
def book(request):
    return HttpResponse('book列表')


def book_detail(request, book_id):
    text = "获取的图示ID为：%s" % book_id
    return HttpResponse(text)
