#--------IMPORTACIONES-------------
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from AppCoder.models import Perfil
from AppCoder.forms import FormularioPerfil
#----Decoradores:
from django.contrib.auth.decorators import login_required
#----LOGIN:
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout


def Home(self):
    plantilla = loader.get_template('AppCoder/home.html')   
    documento = plantilla.render()
    return HttpResponse(documento)

#-------------------LOGIN---------
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(render, request.POST)

        if form.is_valid():
            usuario = request.POST.get('username')
            clave = request.POST.get('password')
            user = authenticate(username=usuario, password=clave)

            if user is not None:
                login(request, user)   
                return render(request, 'AppCoder/home.html', {'mensaje':f'Bienvenido {usuario}'})    
            else:
                return render(request, 'AppCoder/home.html', {'mensaje':'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'AppCoder/home.html', {'mensaje':'Error, Formulario Erroneo'})
    else:
        form = AuthenticationForm()
        return render(request, 'AppCoder/login.html', {'form':form})

#--------------Carga de Formulario-----------
@login_required
def formularioPerfil(request):
    if request.method == 'POST':
        miFormulario = FormularioPerfil(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre = informacion['nombre']
        profesion = informacion['profesion']
        descripcion = informacion['descripcion']
        email = informacion['email']
        perfiles = Perfil(nombre=nombre, profesion=profesion, descripcion=descripcion, email=email)
        perfiles.save()
        return render(request, "AppCoder/home.html")
    else:
        miFormulario = FormularioPerfil()

    return render(request, 'AppCoder/formularioPerfil.html', {'miFormulario':miFormulario})
