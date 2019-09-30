from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# 博客文章的数据模型
from django.utils import timezone


# 每当你修改了models.py文件，都需要用
# python manage.py makemigrations生成迁移文件
# python manage.py migrate将迁移应用到数据中
class ArticlePost(models.Model):
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 标题
    title = models.CharField(max_length=100)

    # 正文
    body = models.TextField()

    # 创建时间
    created = models.DateTimeField(default=timezone.now)

    # 更新时间，自动更新auto_now=True
    updated = models.DateTimeField(auto_now=True)

    # 内部类class Meta提供模型的元数据。
    # 元数据是“任何不是字段的东西”，
    # 例如排序选项ordering、数据库表名db_table、单数和复数名称verbose_name和 verbose_name_plural。
    # 这些信息不是某篇文章私有的数据，而是整张表的共同行为
    # 要不要写内部类是完全可选的，当然有了它可以帮助理解并规范类的行为
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        # 保证了最新文章永远在最顶部位置
        ordering = ('-updated',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title
