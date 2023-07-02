from django import forms
from .models import Usuario, Comentario




class UsuarioForm(forms.ModelForm):

    nombre = forms.CharField(label='Nombre', required=True, min_length=0, max_length=25, widget=forms.TextInput(attrs={'clas':'form-control', 'placeholder':'Introduzca nombre','style': 'display:flex;'}))

    apellido = forms.CharField(label='Apellido', required=True, min_length=0, max_length=25, widget=forms.TextInput(attrs={'clas':'form-control', 'placeholder':'Introduzca apellido', 'style': 'display:flex;'}))

    rut = forms.CharField(label='Rut', required=True, min_length=12, max_length=12, widget=forms.TextInput(attrs={'clas':'form-control', 'placeholder':'Introduzca rut', 'style': 'display: flex;'}))

    correo = forms.EmailField(label='Correo', required=True, min_length=5, max_length=25, widget=forms.EmailInput(attrs={'clas':'form-control', 'placeholder':'Introduzca e-mail','rows':5, 'style': 'display: flex;'}))


    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'rut', 'correo']

class ComentarioForm(forms.ModelForm):

    autor = forms.CharField(label='Autor', required=True, min_length=0, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduzca su Nombre','style': 'display:flex;'}))
    contenido =forms.CharField(label='Contenido', required=True, min_length=0, max_length=500, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduzca su Tema','style': 'display:flex;'}))

    class Meta:
        model = Comentario
        fields = ('autor', 'contenido')