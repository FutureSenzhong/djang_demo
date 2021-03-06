"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

# 正则部署的应用名称,Django2.0之后，app的urls.py必须配置app_name，否则会报错。
from user import views

app_name = 'user'

# article应用的路由配置
urlpatterns = [
    # 用户登录
    path('login/', views.user_login, name='login'),

    # 用户退出
    path('logout/', views.user_logout, name='logout'),

    # 用户注册
    path('register/', views.user_register, name='register'),
]
