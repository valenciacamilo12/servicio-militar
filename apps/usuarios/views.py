from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.usuarios.forms import RegistroUsuarioForm
from django.contrib.auth.models import User

class RegistroUsuario(CreateView):
    model = User
    form_class = RegistroUsuarioForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')