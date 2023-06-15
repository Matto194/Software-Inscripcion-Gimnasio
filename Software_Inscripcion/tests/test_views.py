from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Usuario
from core.forms import UsuarioForm


class UsuarioFormTest(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpass')

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

    def test_home_view_post(self):
        form_data = {
            'nombre': 'Juan',
            'apellido': 'Perez',
            'rut': '123456789012',
            'correo': 'juan.pe@gmail.com',
        }

        # Crear un cliente y autenticar al usuario de prueba
        client = Client()
        client.force_login(self.user)

        response = client.post(reverse('home'), data=form_data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(response.url, '/?ok')  

      

    def test_home_view_post_invalid_form(self):
        form_data = {
            'nombre': 'Juan',
            'apellido': 'Perez',
            'rut': '123',
            'correo': 'juano.cl',
        }

        # Crear un cliente y autenticar al usuario de prueba
        client = Client()
        client.force_login(self.user)

        response = client.post(reverse('home'), data=form_data)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(response.url, '/?error')  

        