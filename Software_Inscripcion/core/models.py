from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=30)
    rut= models.CharField(max_length=30)
    correo = models.EmailField()

    def get_full_name(self):
        return f'{self.nombre} {self.apellido}'