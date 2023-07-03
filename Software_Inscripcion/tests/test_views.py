from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Comentario


class HomeViewTest(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpass')

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

class TemaViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Test', password='Test')

        self.comentario = Comentario.objects.create(
            autor = 'Jorge Rodriguez',
            contenido = 'como verifico que al clickear en un comentario me redirije al tema?',
            comentario_padre = None
        )

    def test_tema_view_get(self):
        url = reverse('tema', kwargs={'parametro': self.comentario.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context['tema'], self.comentario)