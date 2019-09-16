from django.contrib import admin

# Register your models here.


# 我们需要“告诉”Django，后台中需要添加ArticlePost这个数据表供管理
from article.models import ArticlePost

admin.site.register(ArticlePost)
