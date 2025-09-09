from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField('タイトル',max_length=200)
    content = models.TextField('内容')
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    author = models.ForeignKey(
        User,
        verbose_name='作成者',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title