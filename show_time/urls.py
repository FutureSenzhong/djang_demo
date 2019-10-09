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
from show_time.views import home, about, photo, life, study, time, comment

app_name = 'show_time'

# article应用的路由配置
urlpatterns = [
    # 首页
    path('', home.index, name='index'),

    # 文章列表
    path('article-list/', home.article_list, name='article_list'),

    # 文章详情页面
    path('article-detail/<int:aid>/', home.post_detail, name='article_list_detail'),

    # 关于我
    path('about/', about.about, name='about'),

    # 照片墙
    path('photo/', photo.photo, name='photo'),

    # 慢生活
    path('life/', life.life, name='life'),

    # 学无止境
    path('study/', study.study, name='study'),

    # 时间轴
    path('time/', time.time, name='time'),

    # 留言板
    path('comment/', comment.comment, name='comment'),
]
