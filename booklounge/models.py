from django.db import models

class user(models.Model):
    user_id = models.CharField(max_length=20)
    user_password = models.CharField(max_length=16)
    bookclub_list = models.ManyToManyField("bookclub")

class bookclub(models.Model):
    bookclub_name = models.CharField(max_length=200) #북클럽 이름
    user_count = models.IntegerField(default=3) #참가 인원수
    on_offline = models.IntegerField() # 온오프라인 여부, 온라인 0 오프라인 1



