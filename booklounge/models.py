from django.db import models
from bookclublounge.models import *

class User(models.Model):
    email = models.EmailField(max_length=320, unique=True) # 유저 이메일 필드 로컬파트(64자리) + @ + 도메인파트(255자리) = 320
    nickname = models.CharField(max_length=100) # 유저 닉네임 필드
    password = models.CharField(max_length=100) # 유저 비밀번호 필드
    bookclubs = models.ManyToManyField(Bookclub, blank=True) #신청한 북클럽 필드, 다대다 관계





