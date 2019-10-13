from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.


# 博客文章的数据模型
from django.utils import timezone


# 每当你修改了models.py文件，都需要用
# python manage.py makemigrations生成迁移文件
# python manage.py migrate将迁移应用到数据中
from mdeditor.fields import MDTextField


class UserInfo(User):
    """
    用户信息
    """
    telephone = models.CharField(max_length=11, null=True, unique=True, verbose_name='用户电话')
    avatar = models.FileField(default="images/favicon.ico", verbose_name='用户头像')
    blog = models.OneToOneField(to='Blog', to_field='id', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Blog(models.Model):
    """
    博客信息
    """
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(verbose_name='个人博客标题', max_length=255)
    site_name = models.CharField(verbose_name='站点名称', max_length=255)
    theme = models.CharField(verbose_name='博客主题', max_length=255)

    def __str__(self):
        return self.title


class ArticlePost(models.Model):
    """
    博客文章
    """

    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    author = models.ForeignKey(verbose_name='作者', to='UserInfo', to_field='id', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='文章标题')
    desc = models.CharField(max_length=255, verbose_name='文章描述')
    comment_count = models.IntegerField(default=0, verbose_name='评论数量')
    up_count = models.IntegerField(default=0, verbose_name='点赞数')
    down_count = models.IntegerField(default=0, verbose_name='踩数')
    image_count = models.IntegerField(default=0, verbose_name='封面图片数量')
    category = models.ForeignKey(to='Category', to_field='id', on_delete=models.CASCADE)
    # through参数可以指定用作中介的中间模型
    tags = models.ManyToManyField(to="Tag", through='ArticleTag')
    # 正文
    body = MDTextField(verbose_name='文章正文')
    # 封面图片
    image = models.ImageField(null=True, blank=True, verbose_name='封面图片1')
    image2 = models.ImageField(null=True, blank=True, verbose_name='封面图片2')
    image3 = models.ImageField(null=True, blank=True, verbose_name='封面图片3')
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    # 自动更新auto_now=True
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    # 内部类class Meta提供模型的元数据。
    # 元数据是“任何不是字段的东西”，
    # 例如排序选项ordering、数据库表名db_table、单数和复数名称verbose_name和 verbose_name_plural。
    # 这些信息不是某篇文章私有的数据，而是整张表的共同行为
    # 要不要写内部类是完全可选的，当然有了它可以帮助理解并规范类的行为
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        # 保证了最新文章永远在最顶部位置
        ordering = ('-id',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title

    def get_absolute_url(self):
        return 'article/article-detail/%d/' % self.id


class Category(models.Model):
    """
    文章分类表
    """
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(verbose_name='分类标题', max_length=32)

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
    文章标签
    """
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(verbose_name='标签名称', max_length=32)

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    """
    文章分类关系表
    """
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    article = models.ForeignKey(verbose_name='文章', to="ArticlePost", to_field='id', on_delete=models.CASCADE)
    tag = models.ForeignKey(verbose_name='标签', to="Tag", to_field='id', on_delete=models.CASCADE)

    class Meta:
        # 组合唯一约束
        unique_together = [
            ('article', 'tag'),
        ]

    def __str__(self):
        return self.article.title + "---" + self.tag.title


class ArticleUpDown(models.Model):
    """
    点赞表
    """
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(to='UserInfo', to_field='id',null=True, on_delete=models.CASCADE)
    article = models.ForeignKey(to="ArticlePost", to_field='id', null=True, on_delete=models.CASCADE)
    is_up = models.BooleanField(default=True)

    class Meta:
        # 组合唯一约束
        unique_together = [
            ('article', 'user'),
        ]


class Comment(models.Model):
    """
    评论表
    """
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    article = models.ForeignKey(verbose_name='评论文章', to='ArticlePost', to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', to_field='id', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='评论内容', max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    parent_comment = models.ForeignKey(to='Comment', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Banner(models.Model):
    """
    轮播图
    """
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    article = models.ForeignKey(verbose_name='评论文章', to='ArticlePost', to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', to_field='id', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='评论内容', max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    parent_comment = models.ForeignKey(to='Comment', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Link(models.Model):

    """友情链接"""
    id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField('链接名称', max_length=32)
    linkurl = models.URLField('网址', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
