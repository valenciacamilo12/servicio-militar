from django.contrib.auth.models import User
from django import forms

class RegistroUsuarioForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]

        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Email',
            'username': 'Username',
            'password': 'Contraseña',
        }

    def __init__(self, *args, **kwargs):
        super(RegistroUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Nombres'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Apellidos'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Contraseña'})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input100'})