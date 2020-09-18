from django.db import models
from django.utils.timezone import now


class Article(models.Model):
    article_text = models.TextField('文章内容', max_length=200)
    article_title = models.CharField('文章标题', max_length=50)
    article_id = models.AutoField('主键', primary_key=True)
    article_view = models.IntegerField('访问次数', default=0)
    article_create_time = models.DateTimeField('创建时间', default=now)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
# class Comment(models.Model):
