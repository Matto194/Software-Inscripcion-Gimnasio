from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=30)
    rut= models.CharField(max_length=30)
    correo = models.EmailField()

    def get_full_name(self):
        return f'{self.nombre} {self.apellido}'

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    comentario_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')
    
    def __str__(self):
        return self.contenido