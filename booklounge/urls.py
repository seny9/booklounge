from django.urls import path

from . import views

urlpatterns = [
    path('', views.bookloungehome),
    path('login', views.login),
    path('signup', views.signup),
    path('my', views.my),
    path('introduce', views.introduce),

]
