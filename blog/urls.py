from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article_detail/<int:pk>', views.ArticleDetail.as_view(), name='detail'),
]
