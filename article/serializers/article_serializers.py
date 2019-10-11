from rest_framework import serializers  # 引入序列化的模块

from article.models import ArticlePost


class PostSerializers(serializers.ModelSerializer):
    # 重新设定时间格式
    detectionTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    image_total = serializers.IntegerField()

    class Meta:
        model = ArticlePost
        # fields = ("id","ceshiname","number","statusList","detectionTime ")
        fields = "__all__"   # 可以像上面一样定义字段，也可以这样全部

