from django import forms
from .models import Usuario




class UsuarioForm(forms.ModelForm):

    nombre = forms.CharField(label='nombre', required=True, min_length=0, max_length=25, widget=forms.TextInput(attrs={'clas':'form-control', 'placeholder':'Introduzca nombre'}))

    apellido = forms.CharField(label='apellido', required=True, min_length=0, max_length=25, widget=forms.TextInput(attrs={'clas':'form-control', 'placeholder':'Introduzca apellido'}))

    rut = forms.CharField(label='rut', required=True, min_length=12, max_length=12, widget=forms.TextInput(attrs={'clas':'form-control', 'placeholder':'Introduzca rut'}))

    correo = forms.EmailField(label='correo', required=True, min_length=5, max_length=25, widget=forms.EmailInput(attrs={'clas':'form-control', 'placeholder':'Introduzca e-mail','rows':5}))


    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'rut', 'correo']