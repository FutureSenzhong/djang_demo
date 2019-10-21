from django.contrib import admin

# Register your models here.
# 我们需要“告诉”Django，后台中需要添加ArticlePost这个数据表供管理
from django.urls import reverse
from django.utils.html import format_html

from article.models import *


class CategoryAdmin(admin.ModelAdmin):

    def post_count(self, obj):
        print(self, type(obj), obj)
        return obj.post_set.count()

    post_count.short_description = "文章数量"

    # 配置添加完成后的页面显示列表的字段控制
    list_display = [
        'title', 'operator',
    ]
    # 添加页面所以的字段都显示出来用于编辑
    fields = []

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>' + '&nbsp&nbsp&nbsp&nbsp' + '<a href="{}">删除</a>',
            reverse('admin:article_category_change', args=(obj.id,)),
            reverse('admin:article_category_delete', args=(obj.id,)),
        )

    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


class TagAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'operator',
    ]

    # 在文章列表自定义编辑和删除按钮
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>' + '&nbsp&nbsp&nbsp&nbsp' + '<a href="{}">删除</a>',
            reverse('admin:article_tag_change', args=(obj.id,)),
            reverse('admin:article_tag_delete', args=(obj.id,)),
        )

    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'author', 'up_count', 'views', 'created', 'operator',
    ]

    list_display_links = []

    # 配置搜索过滤
    list_filter = ['title', 'category', 'author']
    # 搜索输入框的字段
    search_fields = ['title', 'category__title']

    # 动作相关的配置，是否展示在顶部
    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = False
    exclude = ['author']

    # 在文章列表自定义编辑和删除按钮
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>' + '&nbsp&nbsp&nbsp&nbsp' + '<a href="{}">删除</a>',
            reverse('admin:article_articlepost_change', args=(obj.id,)),
            reverse('admin:article_articlepost_delete', args=(obj.id,)),
        )

    operator.short_description = '操作'

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)


admin.site.register(UserInfo)
admin.site.register(ArticlePost, PostAdmin)
admin.site.register(Photo)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ArticleUpDown)
admin.site.register(Comment)
admin.site.register(Banner)
admin.site.register(Link)


# 自定义后台站点信息
admin.site.site_title = "邓sir的博客后台管理"
admin.site.site_header = "逗逼世界"
admin.site.index_title = "佛系人生"
