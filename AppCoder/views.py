#--------IMPORTACIONES-------------
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from AppCoder.models import Perfil
from AppCoder.forms import FormularioPerfil, UserRegistrationForm, UserEditForm
#----Decoradores:
from django.contrib.auth.decorators import login_required
#----LOGIN:
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
#-----CRUD--------
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy




#--------Inicio--------------
def Home(self):
    plantilla = loader.get_template('AppCoder/home.html')   
    documento = plantilla.render()
    return HttpResponse(documento)

#--------LOGIN---------------
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

#----Carga de Formulario-----
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

#------------CRUD-------------
class PerfilesList(ListView):
    model = Perfil
    template_name = "AppCoder/Perfiles_lista.html"

class PerfilesDetail(DetailView):
    model = Perfil
    template_name = "AppCoder/Perfiles_detail.html"

class PerfilesUpdate(UpdateView):
    model = Perfil
    success_url = reverse_lazy('Perfiles_lista')
    fields = ['nombre', 'profesion', 'descripcion', 'email']

class PerfilesDelete(DeleteView):
    model = Perfil
    success_url = reverse_lazy('Perfiles_lista')

#---------Registro------
def register_request(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'AppCoder/home.html', {'mensaje':f"Usuario {username} creado"})
        else:
            return render(request, 'AppCoder/home.html', {'mensaje':"No se pudeo crear el usuario"})
    else:
        form = UserRegistrationForm()
        return render(request, 'AppCoder/register.html', {'form':form})

#---------Editar User------
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, 'AppCoder/home.html',{'mensaje':f"Datos de {usuario.username} actualizados"})
    else:
        formulario = UserEditForm(initial={'email':usuario.email})
    return render(request, 'AppCoder/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})
 