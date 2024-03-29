from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       PasswordResetForm)
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView, PasswordResetView)
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm


class Register(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('index')
    template_name = 'users/register.html'


class Login(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')
    template_name = 'users/login.html'


class Logout(LogoutView):
    pass


class ChangePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('index')
    template_name = 'users/changePassword.html'


class ResetPassword(PasswordResetView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('index')
    template_name = 'users/resetPassword.html'
