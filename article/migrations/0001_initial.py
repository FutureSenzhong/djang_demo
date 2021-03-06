# Generated by Django 2.1 on 2019-10-13 15:18

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='文章标题')),
                ('desc', models.CharField(max_length=255, null=True, verbose_name='文章描述')),
                ('comment_count', models.IntegerField(default=0, verbose_name='评论数量')),
                ('up_count', models.IntegerField(default=0, verbose_name='点赞数')),
                ('down_count', models.IntegerField(default=0, verbose_name='踩数')),
                ('image_count', models.IntegerField(default=0, verbose_name='封面图片数量')),
                ('views', models.PositiveIntegerField(default=12345, verbose_name='阅读量')),
                ('body', mdeditor.fields.MDTextField(verbose_name='文章正文')),
                ('image', models.ImageField(blank=True, null=True, upload_to='editor/', verbose_name='封面图片1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='editor/', verbose_name='封面图片2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='editor/', verbose_name='封面图片3')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '博客文章',
                'verbose_name_plural': '博客文章',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticlePost', verbose_name='文章')),
            ],
            options={
                'verbose_name': '文章分类关系',
                'verbose_name_plural': '文章分类关系',
            },
        ),
        migrations.CreateModel(
            name='ArticleUpDown',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('is_up', models.BooleanField(default=True)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.ArticlePost', verbose_name='文章')),
            ],
            options={
                'verbose_name': '点赞',
                'verbose_name_plural': '点赞',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('text_info', models.CharField(default='', max_length=50, verbose_name='标题')),
                ('img', models.ImageField(null=True, upload_to='banner/', verbose_name='轮播图')),
                ('link_url', models.URLField(max_length=100, null=True, verbose_name='图片链接')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否是active')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticlePost', verbose_name='评论文章')),
                ('parent_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Comment')),
            ],
            options={
                'verbose_name': '评论管理',
                'verbose_name_plural': '评论管理',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='链接名称')),
                ('linkurl', models.URLField(max_length=255, verbose_name='网址')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=255, verbose_name='图片描述')),
                ('photo', models.ImageField(upload_to='photo/', verbose_name='图片')),
                ('photo1', models.ImageField(upload_to='photo/', verbose_name='图片')),
                ('photo2', models.ImageField(upload_to='photo/', verbose_name='图片')),
                ('photo3', models.ImageField(upload_to='photo/', verbose_name='图片')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '相册',
                'verbose_name_plural': '相册',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=255, verbose_name='网站描述')),
                ('key_word', models.CharField(blank=True, max_length=255, null=True, verbose_name='关键字')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ImageField(upload_to='user/', verbose_name='用户头像')),
                ('reward', models.ImageField(upload_to='user/', verbose_name='打赏图片')),
                ('info', models.TextField(default='', max_length=255, verbose_name='用户介绍')),
                ('vitae', mdeditor.fields.MDTextField(default='', verbose_name='个人简历')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.UserInfo', to_field='id', verbose_name='评论者'),
        ),
        migrations.AddField(
            model_name='articleupdown',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.UserInfo', to_field='id', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='articletag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Tag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='articlepost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.UserInfo', to_field='id', verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='articlepost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='articlepost',
            name='tags',
            field=models.ManyToManyField(through='article.ArticleTag', to='article.Tag', verbose_name='标签'),
        ),
        migrations.AlterUniqueTogether(
            name='articleupdown',
            unique_together={('article', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='articletag',
            unique_together={('article', 'tag')},
        ),
    ]
