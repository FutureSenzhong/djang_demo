from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from rest_framework.throttling import AnonRateThrottle


class CustomPagination(PageNumberPagination):
    """自定义分页器"""

    page_size_query_param = 'size'
    max_page_size = 50


class CustomThrottle(AnonRateThrottle):
    """自定义限流类"""

    THROTTLE_RATES = {'anon': '1000/day'}


class AllowGetAuthentication(BaseAuthentication):
    """自定义的认证类"""

    def authenticate(self, request):
        if request.method == 'GET':
            return AnonymousUser(), None
        return None


class LoginAuthentication(BaseAuthentication):
    """自定义的认证类"""

    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN', '')
        if token:
            user_token = UserToken.objects.filter(token=token).first()
            if user_token:
                return user_token.user, user_token
        raise AuthenticationFailed('请提供有效的身份认证信息')


class CustomPermission(BasePermission):
    """自定义权限验证类"""

    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, AnonymousUser):
            return True
        for role in user.roles.all():
            for priv in role.privileges.all():
                if priv.method == request.method and \
                        request.path.startswith(priv.url):
                    return True
        return False
