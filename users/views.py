from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView, UpdateView

from .forms import RegisterForm


class Register(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('ua')
    template_name = 'users/reg.html'


class Login(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('ua')
    template_name = 'users/authForm.html'


class ChangePassword(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('ua')
    template_name = 'users/changePassword.html'


class ResetPassword(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('ua')
    template_name = 'users/resetPassword.html'
