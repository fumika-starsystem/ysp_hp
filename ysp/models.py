import self as self
from accounts.models import CustomUser
from django.db import models

# Create your models here.


class Ysp(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=100)
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)


    class Meta:
        verbose_name_plural = 'Ysp'


    def __str__(self):
        return self.title

