from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from apps.soldado.models import Soldado, Servicio, Cuerpo
from apps.soldado.forms import SoldadoForm, ServicioForm, CuerpoForm
from django.urls import reverse_lazy


class CreateSoldado(CreateView):
    model = Soldado
    form_class = SoldadoForm
    template_name = 'soldado/soldado_form.html'
    success_url = reverse_lazy('soldado:soldado_listar')


class UpdateSoldado(UpdateView):
    model = Soldado
    form_class = SoldadoForm
    template_name = 'soldado/soldado_form.html'
    success_url = reverse_lazy('soldado:soldado_listar')


class DeleteSoldado(DeleteView):
    model = Soldado
    form_class = SoldadoForm
    template_name = 'soldado/soldado_eliminar.html'
    success_url = reverse_lazy('soldado:soldado_listar')


class ListSoldado(ListView):
    model = Soldado
    template_name = 'soldado/soldado_listar.html'


#-------------------------------------Servicio---------------------------------


class CreateServicio(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'soldado/servicio_form.html'
    success_url = reverse_lazy('soldado:servicio_listar')


class UpdateServicio(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'soldado/servicio_form.html'
    success_url = reverse_lazy('soldado:servicio_listar')


class DeleteServicio(DeleteView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'soldado/servicio_eliminar.html'
    success_url = reverse_lazy('soldado:servicio_listar')


class ListServicio(ListView):
    model = Servicio
    template_name = 'soldado/servicio_listar.html'



#-------------------------------------Cuerpo---------------------------------


class CreateCuerpo(CreateView):
    model = Cuerpo
    form_class = CuerpoForm
    template_name = 'soldado/cuerpo_form.html'
    success_url = reverse_lazy('soldado:cuerpo_listar')


class UpdateCuerpo(UpdateView):
    model = Cuerpo
    form_class = CuerpoForm
    template_name = 'soldado/cuerpo_form.html'
    success_url = reverse_lazy('soldado:cuerpo_listar')


class DeleteCuerpo(DeleteView):
    model = Cuerpo
    form_class = CuerpoForm
    template_name = 'soldado/cuerpo_eliminar.html'
    success_url = reverse_lazy('soldado:cuerpo_listar')


class ListCuerpo(ListView):
    model = Cuerpo
    template_name = 'soldado/cuerpo_listar.html'