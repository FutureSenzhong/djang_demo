from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import ArticlePostViewSet


urlpatterns = [
]

router = DefaultRouter()
viewset_dict = {
    'article': ArticlePostViewSet,
}
for key, value in viewset_dict.items():
    router.register(key, value)
urlpatterns += router.urls
