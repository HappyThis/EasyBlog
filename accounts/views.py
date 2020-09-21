# Create your views here.
import self as self
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.views.generic import FormView

from EasyBlog import settings
from EasyBlog.utils import get_md5, send_email
from accounts.form import LoginForm, RegisterForm


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


class Register(FormView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(False)
            user.is_active = False
            user.source = 'register'
            user.save(True)
            site = get_current_site(self.request).domain
            sign = get_md5(get_md5(settings.SECRET_KEY + str(user.id)))

            if settings.DEBUG:
                site = '127.0.0.1:8000'
            path = reverse('accounts:result')
            url = "http://{site}{path}?type=validation&id={id}&sign={sign}".format(
                site=site, path=path, id=user.id, sign=sign)

            content = """
                                <p>请点击下面链接验证您的邮箱</p>
    
                                <a href="{url}" rel="bookmark">{url}</a>
    
                                再次感谢您！
                                <br />
                                如果上面链接无法打开，请将此链接复制至浏览器。
                                {url}
                                """.format(url=url)
            send_email(
                emailto=[
                    user.email,
                ],
                title='验证您的电子邮箱',
                content=content)

            url = reverse('accounts:result') + \
                  '?type=register&id=' + str(user.id)
            return HttpResponseRedirect(url)

        else:
            return self.render_to_response({
                'form': form
            })


class Result(FormView):
    def get(self, request, *args, **kwargs):
        type = request.GET.get('type')
        id = request.GET.get('id')

        user = get_object_or_404(get_user_model(), id=id)

        if user.is_active:
            return HttpResponseRedirect('/')
        if type and type in ['register', 'validation']:
            if type == 'register':
                content = '''
        恭喜您注册成功，一封验证邮件已经发送到您 {email} 的邮箱，请验证您的邮箱后登录本站。
        '''.format(email=user.email)
                title = '注册成功'
            else:
                c_sign = get_md5(get_md5(settings.SECRET_KEY + str(user.id)))
                sign = request.GET.get('sign')
                if sign != c_sign:
                    return HttpResponseForbidden()
                user.is_active = True
                user.save()
                content = '''
                恭喜您已经成功的完成邮箱验证，您现在可以使用您的账号来登录本站。
                '''
                title = '验证成功'
            return render(request, 'accounts/result.html', {
                'title': title,
                'content': content
            })
        else:
            return HttpResponseRedirect('/')
