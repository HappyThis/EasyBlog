# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from accounts.form import LoginForm


class Login(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('blog:index')

    def get(self, request, *args, **kwargs):
        return render(self.request, template_name=self.template_name)
