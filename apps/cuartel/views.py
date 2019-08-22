from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.cuartel.models import Cuartel, Compania
from apps.cuartel.forms import CuartelForm, CompaniaForm

class CreateCuartel(CreateView):
    model = Cuartel
    form_class = CuartelForm
    template_name = 'cuartel/cuartel_form.html'
    success_url = reverse_lazy('cuartel:cuartel_listar')


class UpdateCuartel(UpdateView):
    model = Cuartel
    form_class = CuartelForm
    template_name = 'cuartel/cuartel_form.html'
    success_url = reverse_lazy('cuartel:cuartel_listar')


class DeleteCuartel(DeleteView):
    model = Cuartel
    form_class = CuartelForm
    template_name = 'cuartel/cuartel_eliminar.html'
    success_url = reverse_lazy('cuartel:cuartel_listar')


class ListCuartel(ListView):
    model = Cuartel
    template_name = 'cuartel/cuartel_listar.html'


#-------------------------compañia---------------------------------------------


class CreateCompania(CreateView):
    model = Compania
    form_class = CompaniaForm
    template_name = 'cuartel/compania_form.html'
    success_url = reverse_lazy('cuartel:compania_listar')


class UpdateCompania(UpdateView):
    model = Compania
    form_class = CompaniaForm
    template_name = 'cuartel/compania_form.html'
    success_url = reverse_lazy('cuartel:compania_listar')


class DeleteCompania(DeleteView):
    model = Compania
    form_class = CompaniaForm
    template_name = 'cuartel/compania_eliminar.html'
    success_url = reverse_lazy('cuartel:compania_listar')


class ListCompania(ListView):
    model = Compania
    template_name = 'cuartel/compania_listar.html'
