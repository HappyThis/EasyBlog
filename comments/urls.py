from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path(
        'content/<int:article_pk>/',
        views.CommentView.as_view(),
        name='comment'),
    path(
        'content/<int:article_pk>/<int:comment_id>',
        views.ReplyComment.as_view(),
        name='reply'),
]
