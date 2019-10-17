from django_filters import rest_framework as drf
from article.models import ArticlePost


class ArticlePostFilter(drf.FilterSet):
    """自定义经理人数据过滤器"""

    title = drf.CharFilter(lookup_expr='istartswith')
    views = drf.NumberFilter(field_name='servstar', lookup_expr='gte')

    class Meta:
        model = ArticlePost
        fields = ('title', 'views')
