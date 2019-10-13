import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from article.models import Banner
from article.serializers.article_serializers import BannerSerializers


def index(request):
    if request.method == 'GET':
        return render(request, 'article/index.html')


def get_banner(request):
    if request.method == 'GET':
        banners = Banner.objects.all()
        if banners:
            json_data = BannerSerializers(banners, many=True)
            json_banner = json_data.data
            # 数据组合成json传递给templates模板使用
            data = {'data': json_banner, 'status_code': 200}

            # 渲染模板文件展示数据
            return HttpResponse(json.dumps(data))
