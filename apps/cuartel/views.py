from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.cuartel.models import Cuartel, Compania
from apps.cuartel.forms import CuartelForm, CompaniaForm

# Reportes PDF
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import View
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.platypus import TableStyle, Table
from reportlab.lib.units import cm
from reportlab.lib import colors

# Reportes PDF

class ReporteCuartelPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/image_5.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE CUARTELES")

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
        encabezado = ('ID', 'Nombre del cuartel', 'Direccion')
        detalle = [(cuartel.id_cuartel, cuartel.nombre, cuartel.direccion) for cuartel in Cuartel.objects.all()]
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

class ReporteCompaniaPDF(View):

    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/image_5.jpg'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"REPORTE DE COMPAÑIAS")

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
        encabezado = ('ID compañia', 'Actividad')
        detalle = [(compania.id_compania, compania.actividad) for compania in Compania.objects.all()]
        detalle_orden = Table([encabezado] + detalle, colWidths=[4 * cm, 4 * cm, 4 * cm, 4 * cm])
        detalle_orden.setStyle(TableStyle(
            (
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 0), (-1, -1), 10)
            )
        ))

        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)

# ------------------------------------- Cuartel -----------------------------------------------------------------------

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
