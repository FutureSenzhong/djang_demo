from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from user.forms import UserLoginForm


# 登陆视图函数
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)

        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            # Form不仅负责验证数据，还可以“清洗”它：将其标准化为一致的格式，
            # 这个特性使得它允许以各种方式输入特定字段的数据，并且始终产生一致的输出。
            # 一旦Form使用数据创建了一个实例并对其进行了验证，就可以通过cleaned_data属性访问清洗之后的数据
            data = user_login_form.cleaned_data

            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            # authenticate()方法验证用户名称和密码是否匹配，如果是，则将这个用户数据返回。
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # login()方法实现用户登录，将用户数据保存在session中
                login(request, user)
                # 登陆成功，返回主页
                return redirect("article:article_list")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        data = {'user_login_form': user_login_form}
        return render(request, 'user/login.html', data)
    else:
        return HttpResponse("请使用GET或POST请求数据")
