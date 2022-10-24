from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here
class User(AbstractUser):
    profile = models.TextField(max_length=500, blank=True) #하나하나 입력값 = django 모델에 들어가있다.