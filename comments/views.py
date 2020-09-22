from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView

from accounts.models import BlogUser
from blog.models import Article
from comments.form import PostComment
from comments.models import Comment


class CommentView(FormView):
    template_name = 'comments/article_comment.html'
    form_class = PostComment

    def get(self, request, *args, **kwargs):
        article_pk = self.kwargs['article_pk']
        comment_query_list = Comment.objects.filter(article=article_pk)
        return render(request, template_name=self.template_name,
                      context={'comment_list': comment_query_list, 'article_id': article_pk, 'form': PostComment()})

    def form_valid(self, form):
        if self.request.user.is_authenticated:

            article = Article.objects.filter(article_id=self.kwargs['article_pk']).first()

            comment = Comment.objects.create()
            user = self.request.user
            new_comment = Comment.objects.create(article=article, user=user,
                                                 comment_text=form.cleaned_data['comment_text'])
            new_comment.save()
            return HttpResponseRedirect(reverse('comments:comment', args=[self.kwargs['article_pk']]))
        else:
            return HttpResponseRedirect(reverse('accounts:login'))


class ReplyComment(FormView):
    template_name = 'comments/comment_reply.html'
    form_class = PostComment

    def get(self, request, *args, **kwargs):
        article_id = self.kwargs['article_pk']
        comment_id = self.kwargs['comment_id']
        return render(request, template_name=self.template_name,
                      context={'article_id': article_id, 'comment_id': comment_id, 'form': PostComment()})

    def form_valid(self, form):
        if self.request.user.is_authenticated:

            article = Article.objects.filter(article_id=self.kwargs['article_pk']).first()

            comment = Comment.objects.filter(comment_id=self.kwargs['comment_id']).first()
            user = self.request.user
            new_comment = Comment.objects.create(article=article, user=user, replyer=comment,
                                                 comment_text=form.cleaned_data['comment_text'])
            new_comment.save()
            return HttpResponseRedirect(reverse('comments:comment', args=[self.kwargs['article_pk']]))
        else:
            return HttpResponseRedirect(reverse('accounts:login'))
