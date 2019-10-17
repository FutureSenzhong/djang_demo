from rest_framework import serializers

from article.models import ArticlePost, Category, UserInfo


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ArticlePostSerializer(serializers.ModelSerializer):

    author = UserInfoSerializer()
    category = CategorySerializer()

    class Meta:
        model = ArticlePost
        fields = '__all__'
