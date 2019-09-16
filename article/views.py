from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# 编写第一个Hello Django视图程序
def article_list(request):
    return HttpResponse('Hello Django')

