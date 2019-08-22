from apps.cuartel.models import Compania,Cuartel
from django import forms


class CompaniaForm(forms.ModelForm):
    class Meta:
        model = Compania

        fields = [
            'actividad',
        ]

        labels = {
            'actividad': 'Actividad',
        }

        widgets = {
            'actividad': forms.TextInput(attrs={'class':'form-class'}),
        }



class CuartelForm(forms.ModelForm):
    class Meta:
        model = Cuartel

        fields = [
            'nombre',
            'direccion',
        ]

        labels = {
            'nombre': 'Nombre',
            'direccion': 'Direccion',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-class'}),
            'direccion': forms.TextInput(attrs={'class': 'form-class'}),
        }