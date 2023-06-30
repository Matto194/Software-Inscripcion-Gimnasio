from django.contrib import admin
from .models import Usuario, Comentario

# Register your models here.

@admin.register(Usuario)  
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'rut', 'correo')  

admin.site.register(Comentario)