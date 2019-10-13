from django.contrib import admin

# Register your models here.


# 我们需要“告诉”Django，后台中需要添加ArticlePost这个数据表供管理
from article.models import *

admin.site.register(UserInfo)
admin.site.register(Blog)
admin.site.register(ArticlePost)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ArticleUpDown)
admin.site.register(Comment)
admin.site.register(Banner)
admin.site.register(Link)
