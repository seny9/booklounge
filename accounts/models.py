from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.managers import UserManager
from bookclublounge.models import Bookclub

class User(AbstractUser):
    #장고가 지원하는 User모델 필드 외의 것 적어준다

    # username = None #username 사용하지 않는 경우
    # email = models.EmailField('', max_length=320, unique=True) # 유저 이메일 필드 로컬파트(64자리) + @ + 도메인파트(255자리) = 320
    nickname = models.CharField('', max_length=100, unique=True) # 유저 닉네임 필드
    # password = models.CharField('', max_length=100) # 유저 비밀번호 필드
    bookclubs = models.ManyToManyField(Bookclub, blank=True) #신청한 북클럽 필드, 다대다 관계

    # 이메일을 유저네임 필드로 사용
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['nickname']
    #
    # objects = UserManager()

    def __str__(self):
        return '이메일 : ' + self.email + ", 닉네임 : " + self.nickname




