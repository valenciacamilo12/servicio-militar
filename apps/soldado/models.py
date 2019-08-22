from django.db import models
from apps.cuartel.models import Compania, Cuartel
from django.utils.translation import ugettext as _

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.descripcion)

class Cuerpo(models.Model):
    id_cuerpo = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.denominacion)

class Soldado(models.Model):
    id_soldado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    grado = models.CharField(max_length=40)
    servicio = models.ForeignKey(Servicio, blank=True, null=True, on_delete=models.CASCADE)
    cuerpo = models.ForeignKey(Cuerpo, blank=True, null=True, on_delete=models.CASCADE)
    compania = models.ForeignKey(Compania, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)


    class Meta:
        permissions = {
            ('is_dos', _('Usuario Dos')),
        }
