from django.db import models
from django.utils.timezone import now

from accounts.models import BlogUser
from blog.models import Article


class Comment(models.Model):
    comment_id = models.AutoField('主键', primary_key=True)
    comment_text = models.TextField('正文', max_length=300)
    comment_create_time = models.DateTimeField('创建时间', default=now)
    # Article外键
    article = models.ForeignKey(Article, models.CASCADE, verbose_name='文章', blank=True, null=True)
    # User外键
    user = models.ForeignKey(BlogUser, models.CASCADE, verbose_name='用户', blank=True, null=True)
    # 回复者
    replyer = models.ForeignKey('self', models.CASCADE, verbose_name='回复谁?', blank=True, null=True)

    class Meta:
        ordering = ['comment_id']
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        get_latest_by = 'comment_id'
