from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm


class Register(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('ua')
    template_name = 'users/reg.html'

class Login(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('ua')
    template_name = 'users/authForm.html'
