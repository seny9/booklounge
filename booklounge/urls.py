from django.urls import path

from . import views

urlpatterns = [
    path('', views.bookloungehome),
    path('my', views.my),
    path('introduce', views.introduce),

]
