from django.db import models
from django.utils import timezone

class Bookclub(models.Model):
    name = models.CharField(max_length=200) # 북클럽 이름 필드
    description = models.TextField(max_length=2000) # 북클럽 세부내용 필드

    #초이스 선택옵션 추가, 인원수 3명부터 10명까지 가능
    MAXUSER_CHOICES = zip( range(3,11), range(3,11) )
    user_max = models.IntegerField(choices=MAXUSER_CHOICES) # 북클럽 참가 인원수 필드, choice기능 사용

    #초이스 선택옵션 추가, ON -> 온라인 북클럽, OFF ->오프라인 북클럽
    ONOFFLINE_CHOICES = (('ON', '온라인'),
                         ('OFF', '오프라인'))
    on_offline = models.CharField(max_length=3, choices=ONOFFLINE_CHOICES) # 북클럽 온오프라인 여부 필드, choice기능 사용

    pub_date = models.DateTimeField('date published')


