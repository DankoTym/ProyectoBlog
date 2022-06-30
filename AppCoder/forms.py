from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class FormularioPerfil(forms.Form):
    nombre=forms.CharField(max_length=15)          #nombre visible
    profesion=forms.CharField(max_length=20)       #area laboral a la que pertenece
    descripcion=forms.CharField(max_length=250)    #una auto presentación 
    email=forms.EmailField()