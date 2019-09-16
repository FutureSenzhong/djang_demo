"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

# 正则部署的应用名称,Django2.0之后，app的urls.py必须配置app_name，否则会报错。
from article import views

app_name = 'article'

# article应用的路由配置
urlpatterns = [
    # 文章列表
    path('article-list/', views.article_list, name='article_list'),

    # 文章详情页面
    path('article-detail/<int:article_id>/', views.article_detail, name='article_detail'),

    # 写文章
    path('article-create/', views.article_create, name='article_create'),

    # 删除文章
    path('article-delete/<int:article_id>/', views.article_delete, name='article_delete'),
]
