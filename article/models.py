from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# 博客文章的数据模型
from django.utils import timezone


class ArticlePost(models.Model):
    # 作者
    author = models.Foreignkey(User, on_delete=models.CASCADE)

    # 标题
    title = models.CharField(max_length=100)

    # 正文
    body = models.TextField()

    # 创建时间
    created = models.DateTimeField(default=timezone.now)

    # 更新时间，自动更新auto_now=True
    updated = models.DateTimeField(auto_now=True)

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title
