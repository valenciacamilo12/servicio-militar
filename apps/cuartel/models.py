from django.db import models

class Compania(models.Model):
    id_compania = models.AutoField(primary_key=True)
    actividad = models.CharField(max_length=40)


class Cuartel(models.Model):
    id_cuartel = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)

