from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass  # 사용자 모델을 확장하려면 필드 추가

class SomeModel(models.Model):
    user = models.ForeignKey("gwc.CustomUser", on_delete=models.CASCADE)  # 올바른 참조 방식