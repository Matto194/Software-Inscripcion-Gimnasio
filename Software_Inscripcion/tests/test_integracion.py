# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User
# from core.models import Usuario, Comentario

# class IntegrationTest(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.url_home = reverse('home')
#         self.url_foro = reverse('foro')
#         self.url_tema = reverse('tema', kwargs={'parametro': 1})
#         self.usuario_data = {
#             'nombre': 'John',
#             'apellido': 'Doe',
#             'rut': '1234567890',
#             'correo': 'john.doe@example.com'
#         }
#         self.comentario_data = {
#             'autor': 'John Doe',
#             'contenido': 'Este es un comentario de prueba'
#         }

#     def test_creacion_usuario(self):
#         # Autenticar al usuario
#         User.objects.create_user(username='testuser', password='testpass')
#         self.client.login(username='testuser', password='testpass')

#         response = self.client.post(self.url_home, data=self.usuario_data)
#         self.assertEqual(response.status_code, 302)  # Verifica que se redirija correctamente
#         self.assertEqual(Usuario.objects.count(), 1)  # Verifica que se haya creado un nuevo usuario

#     def test_creacion_comentario(self):
#         response = self.client.post(self.url_foro, data=self.comentario_data)
#         self.assertEqual(response.status_code, 302)  # Verifica que se redirija correctamente
#         self.assertEqual(Comentario.objects.count(), 1)  # Verifica que se haya creado un nuevo comentario

#     def test_respuesta_comentario(self):
#         comentario_padre = Comentario.objects.create(autor='Padre', contenido='Comentario padre')
#         self.comentario_data['comentario_padre'] = comentario_padre.id
#         response = self.client.post(self.url_tema, data=self.comentario_data)
#         self.assertEqual(response.status_code, 302)  # Verifica que se redirija correctamente
#         self.assertEqual(Comentario.objects.count(), 2)  # Verifica que se haya creado una nueva respuesta
