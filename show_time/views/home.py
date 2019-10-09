import json

import markdown
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.


# 编写第一个Hello Django视图程序
from article.forms import ArticlePostForm
from article.models import ArticlePost
from my_blog.settings import MARKDOWN_EXTENSIONS
from show_time.serializers.article_serializers import PostSerializers


def index(request):
    if request.method == 'GET':
        return render(request, 'show_time/index.html')


def article_list(request):
    per_page = int(request.GET.get('per_page', 5))
    curr_page = int(request.GET.get('curr_page', 0))
    # hello django
    # return HttpResponse('Hello Django')

    # 获取指定页的数据
    articles = ArticlePost.objects.all()[curr_page*per_page:(curr_page+1)*per_page]

    # 分页
    # 总数量
    total = ArticlePost.objects.count()

    # 判断是否查询到数据
    if articles:
        # 序列化
        json_data = PostSerializers(articles, many=True)
        # 数据组合成json传递给templates模板使用
        data = {'data': json_data.data, 'total': total, 'status_code': 200}

        # 渲染模板文件展示数据
        return HttpResponse(json.dumps(data))
    else:
        data = {'data': '', 'total': total, 'status_code': 404}
        return HttpResponse(json.dumps(data))


# 文章详情
# def article_detail(request, article_id):
#     # 取出相应的文章
#     article = ArticlePost.objects.get(id=article_id)
#     # 需要传递给模板的对象
#     data = {'article': article}
#     # 载入模板，并返回context对象
#     return render(request, 'article/detail.html', data)


# 使用markdown编辑插件显示有格式的文章详情页面
def post_detail(request, aid):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=aid)

    # markdown格式的文章内容
    article.body = markdown.markdown(article.body, extensions=MARKDOWN_EXTENSIONS)
    # 需要传递给模板的对象
    data = {'article': article}
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', data)


# 写文章的视图
def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("article:article_list")
        # 如果数据不合法，返回错误信息
        else:
            # return HttpResponse("表单内容有误，请重新填写。")
            return HttpResponse("")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        data = {'article_post_form': article_post_form}
        # 返回模板
        return render(request, 'article/create.html', data)


# 删文章
# def article_delete(request, article_id):
#     # 根据 id 获取需要删除的文章
#     article = ArticlePost.objects.get(id=article_id)
#     # 调用.delete()方法删除文章
#     article.delete()
#     # 完成删除后返回文章列表
#     return redirect("article:article_list")


# 安全删除
# 安全删除文章
def article_safe_delete(request, article_id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=article_id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("")
        # return HttpResponse("仅允许post请求")


# 更新文章
def article_update(request, article_id):
    """
    更新文章的视图函数
    通过POST方法提交表单，更新titile、body字段
    GET方法进入初始表单页面
    id： 文章的 id
    """

    # 获取需要修改的具体文章对象
    article = ArticlePost.objects.get(id=article_id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect("article:article_detail", article_id=article_id)
        # 如果数据不合法，返回错误信息
        else:
            # return HttpResponse("表单内容有误，请重新填写。")
            return HttpResponse("")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        data = {'article': article, 'article_post_form': article_post_form}
        # 将响应返回到模板中
        return render(request, 'article/update.html', data)
