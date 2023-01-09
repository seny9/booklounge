from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = 'accounts'
urlpatterns=[
    # path('', views.index, name='index'),
    path('login', views.login),
    path('signup', views.signup),
    path('logout', views.logout, name='logout'),
]