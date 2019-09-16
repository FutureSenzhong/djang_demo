import markdown
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.


# 编写第一个Hello Django视图程序
from article.forms import ArticlePostForm
from article.models import ArticlePost
from my_blog.settings import MARKDOWN_EXTENSIONS


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
# def article_detail(request, article_id):
#     # 取出相应的文章
#     article = ArticlePost.objects.get(id=article_id)
#     # 需要传递给模板的对象
#     data = {'article': article}
#     # 载入模板，并返回context对象
#     return render(request, 'article/detail.html', data)


# 使用markdown编辑插件显示有格式的文章详情页面
def article_detail(request, article_id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=article_id)

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
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form}
        # 返回模板
        return render(request, 'article/create.html', context)


# 删文章
def article_delete(request, article_id):
    # 根据 id 获取需要删除的文章
    article = ArticlePost.objects.get(id=article_id)
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("article:article_list")
