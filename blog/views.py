import modes as modes
from django.forms import models
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from blog.models import Article


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    model = Article


class ArticleDetail(generic.DeleteView):
    template_name = 'blog/detail.html'
    model = Article
    context_object_name = 'article'

    def get_object(self, queryset=None):
        # 从request中获取字段
        pk = self.kwargs['article_pk']
        # 访问数量自增
        article = Article.objects.get(article_id=pk)
        article.article_view += 1
        # 查询
        return article


