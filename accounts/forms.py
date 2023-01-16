from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#유저정보 가입폼
class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "nickname")


# 유저정보 로그인폼
class LoginForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("email", "password")

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
        
#유저정보 수정폼
class UpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email", "nickname")
