from django.contrib.auth import logout, login
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import RedirectView, FormView

from authentication.forms import LoginForm


class LogoutView(RedirectView):
    pattern_name = 'homepage'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class LoginView(FormView):
    template_name = 'authentication/user_login.html'
    success_url = reverse_lazy('homepage')
    form_class = LoginForm

    def get_context_data(self, *args, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['active_page'] = 'login'
        return context

    def form_valid(self, form):
        user = form.login()
        if user is not None:
            login(self.request, user)
            return JsonResponse({'state': 'success'})
        else:
            return JsonResponse({'state': 'error', 'msg': '用户名或密码错误'})
