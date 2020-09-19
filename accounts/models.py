from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class BlogUser(AbstractUser):
    user_nickname = models.CharField('昵称', max_length=100, blank=True)
    user_create_time = models.DateTimeField('创建时间', default=now)

    class Meta:
        ordering = ['-id']
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
