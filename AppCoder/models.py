from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
       
    nombre=models.CharField(max_length=15)          #nombre visible
    profesion=models.CharField(max_length=20)       #area laboral a la que pertenece
    descripcion=models.CharField(max_length=250)    #una auto presentación 
    email=models.EmailField()

    def __str__(self) -> str:
        return self.nombre+" -Profesión: "+str(self.profesion)