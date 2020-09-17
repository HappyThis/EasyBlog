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
        pk = self.kwargs['pk']
        # 查询
        return Article.objects.get(article_id=pk)
