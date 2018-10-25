#coding=utf-8
def test(request):
    return None
from django.http import HttpResponse


def user_view(request):
    return HttpResponse('123')