from django.shortcuts import render

# Create your views here.


# 编写第一个Hello Django视图程序
from article.models import ArticlePost


def article_list(request):
    # hello django
    # return HttpResponse('Hello Django')

    # 查询取出所有的文章
    articles = ArticlePost.objects.all()

    # 数据组合成json传递给templates模板使用
    data = {'articles': articles}

    # 渲染模板文件展示数据
    return render(request,  'article/list.html', data)


# 文章详情
def article_detail(request, article_id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=article_id)
    # 需要传递给模板的对象
    data = {'article': article}
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', data)
