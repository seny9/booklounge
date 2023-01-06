from django.urls import path

from .import views

urlpatterns=[
    path('', views.bookclubhome),
    path('bookclub/<str:name>', views.showBookclub),

]
