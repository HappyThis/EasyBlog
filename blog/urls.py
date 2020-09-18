from django.contrib import admin
from django.urls import path, include

from blog import views

app_name='blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article_detail/<int:article_pk>', views.ArticleDetail.as_view(), name='detail'),
#    path('article_comment/<int:pk>', views.ArticleComment.as_view(), name='comment'),
]
