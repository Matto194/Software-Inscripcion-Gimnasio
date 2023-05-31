from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm
from django.urls import reverse
from .models import Usuario

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

    return render(request,'core/base.html', {'form':usuario_form,'usuarios':usuarios})

def prueba(request):
    return render(request, 'core/home.html')

