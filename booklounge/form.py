from django.forms import ModelForm
from booklounge.models import *

class userForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'nickname', 'password']
