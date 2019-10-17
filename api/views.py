from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from api.filters import ArticlePostFilter
from api.helpers import CustomPermission, AllowGetAuthentication, LoginAuthentication
from api.serializers import ArticlePostSerializer
from article.models import ArticlePost


class ArticlePostViewSet(CacheResponseMixin, ModelViewSet):
    queryset = ArticlePost.objects.all()\
        .prefetch_related('category')\
        .prefetch_related('author')\
        .order_by('created')
    serializer_class = ArticlePostSerializer
    # authentication_classes = (AllowGetAuthentication, LoginAuthentication)
    # permission_classes = (CustomPermission, )
    filter_backends = (DjangoFilterBackend, )
    # filterset_class = ArticlePostFilter

