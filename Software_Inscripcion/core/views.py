from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm
from django.urls import reverse
from .models import Usuario
from .models import Comentario
from .forms import ComentarioForm


# Create your views here.
@login_required
def home(request):
    usuario_form = UsuarioForm()
    usuarios = Usuario.objects.all()

    if request.method == 'POST':
        usuario_form = UsuarioForm(data=request.POST)

        if usuario_form.is_valid():
            usuario_form.save()
            return redirect(reverse('home')+'?ok')
        else:
            return redirect(reverse('home')+'?error') 

    return render(request,'core/index.html', {'form':usuario_form,'usuarios':usuarios})

def comentarios(request):
    comentarios = Comentario.objects.all()
    comentario_form = ComentarioForm()
    
    if request.method == 'POST':
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():
            comentario_form.save()
            return redirect(reverse('foro')+'?ok')
        else:
            return redirect(reverse('foro')+'?error') 
    else:
        comentario_form = ComentarioForm()
    return render(request, 'core/foro.html', {'form':comentario_form, 'comentarios': comentarios})

def tema(request, parametro):
    tema_especifico = Comentario.objects.get(id=parametro)

    return render(request,'core/respuestas.html', {'tema': tema_especifico})