from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    """用户登陆表单继承django的forms.Form类
    在前面发表文章的模块中，表单类继承了forms.ModelForm，
    这个父类适合于需要直接与数据库交互的功能，比如新建、更新数据库的字段等。
    如果表单将用于直接添加或编辑Django模型，则可以使用 ModelForm来避免重复书写字段描述。
    而forms.Form则需要手动配置每个字段，它适用于不与数据库进行直接交互的功能。
    用户登录不需要对数据库进行任何改动，因此直接继承forms.Form就可以了。
    """

    username = forms.CharField()
    password = forms.CharField()


# 注册用户表单
class UserRegisterForm(forms.ModelForm):
    """
    继承forms.ModelForm，可以自动生成模型中已有的字段
    """
    # 复写 User 的密码
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        # 覆写某字段之后，内部类class Meta中的定义对这个字段就没有效果了，所以fields不用包含password
        fields = ('username', 'email')

    # 对两次输入的密码是否一致进行检查
    # 验证密码一致性方法不能写def
    # clean_password()，因为如果你不定义def
    # clean_password2()
    # 方法，会导致password2中的数据被Django判定为无效数据从而清洗掉，从而password2属性不存在。
    # 最终导致两次密码输入始终会不一致，并且很难判断出错误原因
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")

