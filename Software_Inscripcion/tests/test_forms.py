from django.test import TestCase
from django.urls import reverse
from core.forms import ComentarioForm, UsuarioForm

class ComentarioFormTest(TestCase):

    def test_comentario_form_valid(self):
        form_data = {
            'autor': 'Jorge Rodriguez',
            'contenido': 'Como compruebo que un test esta correcto?'
        } 
        form = ComentarioForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comentario_form_invalid(self):
        form_data = {
            'autor': 'a',
            'contenido': ''
        }
        form = ComentarioForm(data=form_data)
        self.assertFalse(form.is_valid())

class UsuarioFormTest(TestCase):
    def test_usuario_form_valid(self):
        form_data = {
            'nombre': 'Juan',
            'apellido': 'Perez',
            'rut': '123456789012',
            'correo': 'juan.pe@gmail.com',
        }
        form = UsuarioForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_invalid(self):
        form_data = {
            'nombre': 'Juan',
            'apellido': 'Perez',
            'rut': '123',
            'correo': 'juano.cl',
        }
        form = UsuarioForm(data=form_data)
        self.assertFalse(form.is_valid())