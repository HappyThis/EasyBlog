from django.contrib import admin
from django.urls import path, include

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('result/', views.Result.as_view(), name='result'),
]
