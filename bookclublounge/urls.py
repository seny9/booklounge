from django.urls import path

from .import views

urlpatterns=[
    path('', views.bookclubhome),
    path('login/', views.login),
    path('bookclub/<str:name>', views.showBookclub, name='showdetail'),

]
