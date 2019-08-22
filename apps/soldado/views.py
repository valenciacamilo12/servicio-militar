from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from apps.soldado.forms import SoldadoForm, ServicioForm, CuerpoForm
from django.urls import reverse_lazy
from apps.soldado.models import Soldado, Servicio, Cuerpo

# Reportes PDF
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import View
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors



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


# Reportes del directorio soldado

class ReporteSoldadoPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/image_5.jpg'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE SOLDADOS")

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 550
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezado = ('Nombre', 'Apellido', 'Grado', 'Servicio', 'Compañia')
        detalle = [(soldado.nombre, soldado.apellido, soldado.grado, soldado.servicio, soldado.compania) for soldado in Soldado.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[3 * cm, 3 * cm, 3 * cm, 3 * cm])
        detalle_orden.setStyle(TableStyle(
            (
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            )
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)

class ReporteServicioPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/image_5.jpg'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE SERVICIOS")

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 550
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezado = ('Id del servicio', 'Descripcion')
        detalle = [(servicio.id_servicio, servicio.descripcion) for servicio in Servicio.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[4 * cm, 4 * cm, 4 * cm, 4 * cm])
        detalle_orden.setStyle(TableStyle(
            (
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            )
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)

class ReporteCuerpoPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/image_5.jpg'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE CUERPOS MILITARES")

    def get(self, request):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 550
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        encabezado = ('Id del cuerpo', 'Denominacion')
        detalle = [(cuerpo.id_cuerpo, cuerpo.denominacion) for cuerpo in Cuerpo.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[4 * cm, 4 * cm, 4 * cm, 4 * cm])
        detalle_orden.setStyle(TableStyle(
            (
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            )
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)

