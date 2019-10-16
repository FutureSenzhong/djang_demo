from django.contrib import admin

# Register your models here.


# 我们需要“告诉”Django，后台中需要添加ArticlePost这个数据表供管理
from article.models import *

admin.site.register(UserInfo)
admin.site.register(ArticlePost)
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ArticleUpDown)
admin.site.register(Comment)
admin.site.register(Banner)
admin.site.register(Link)


# 自定义后台站点信息
admin.site.site_title = "邓sir的博客后台管理"
admin.site.site_header = "逗逼世界"
admin.site.index_title = "佛系人生"
