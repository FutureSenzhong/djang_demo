from rest_framework import serializers  # �������л���ģ��

from article.models import *


class PostSerializers(serializers.ModelSerializer):
    # �����趨ʱ���ʽ
    detectionTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    image_total = serializers.IntegerField()

    class Meta:
        model = ArticlePost
        # fields = ("id","ceshiname","number","statusList","detectionTime ")
        fields = "__all__"   # ����������һ�������ֶΣ�Ҳ��������ȫ��


class BannerSerializers(serializers.ModelSerializer):
    # �����趨ʱ���ʽ

    class Meta:
        model = Banner
        fields = "__all__"   # ����������һ�������ֶΣ�Ҳ��������ȫ��
