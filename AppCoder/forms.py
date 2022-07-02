from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class FormularioPerfil(forms.Form):
    nombre=forms.CharField(max_length=15)          #nombre visible
    profesion=forms.CharField(max_length=20)       #area laboral a la que pertenece
    descripcion=forms.CharField(max_length=250)    #una auto presentación 
    email=forms.EmailField()

#------REGISTRO----------
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

class Meta:
    model = User   
    fields = {'username', 'password1', 'password2', 'email'}
    help_text = {k:"" for k in fields}

#----------Edición de User----------
class UserEditForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

class Meta:
    model = User    
    fields = {'email', 'password1', 'password2'}
    help_text = {k:"" for k in fields}