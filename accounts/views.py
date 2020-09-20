# Create your views here.
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from accounts.form import LoginForm


class Login(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        print("matched")
        auth.login(self.request, form.get_user())
        #        auth.logout(self.request)
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        print("not matched")
        return self.render_to_response({
            'form': form
        })
