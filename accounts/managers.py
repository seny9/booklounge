from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager): #username이 아닌 email을 로그인아이디로 하는 커스텀매니저

    def _create_user(self, email, nickname, password, **extra_fields): # 일반 유저 생성
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        nickname = self.normalize_email(nickname)
        user = self.model(email=email, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, nickname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, nickname, password, **extra_fields)

    def create_superuser(self, email, nickname, password, **extra_fields): # 관리자 유저 생성, 스태프, 슈퍼유저 권한
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, nickname, password, **extra_fields)