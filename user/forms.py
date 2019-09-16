from django import forms


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


