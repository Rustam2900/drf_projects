from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('foydalanuchi')
        verbose_name_plural = _('foydalanuchilar')

