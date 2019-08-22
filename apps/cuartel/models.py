from django.db import models
from django.utils.translation import ugettext as _

class Compania(models.Model):
    id_compania = models.AutoField(primary_key=True)
    actividad = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.actividad)


class Cuartel(models.Model):
    id_cuartel = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        permissions = {
            ('is_uno', _('Usuario Uno')),
        }
