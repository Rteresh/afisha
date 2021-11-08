from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя '
    }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Введите пароль'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя '
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите ваш электронный адресс'
    }))
    password1 = forms.CharField(widget = forms.PasswordInput(
        attrs={
            'placeholder': 'Введите пароль'

        }
    ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Подтвердите ваш пароль'
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

