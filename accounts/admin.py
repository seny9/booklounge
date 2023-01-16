from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import SignupForm, UpdateForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = SignupForm
    form = UpdateForm
    model = User
    list_display = ['username', 'email', 'nickname']


admin.site.register(User, CustomUserAdmin)
