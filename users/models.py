from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('foydalanuchi')
        verbose_name_plural = _('foydalanuchilar')


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name=('title'))
    description = models.TextField(blank=True, null=True, verbose_name=('description'))
    image = models.ImageField(blank=True, null=True, verbose_name=('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=('updated at'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
