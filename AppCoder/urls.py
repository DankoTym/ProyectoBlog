from django.contrib import admin
from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Home, name="home"),
    path('FormularioPerfil/', views.formularioPerfil, name="FormularioPerfil"),
    #--LOGIN--
    path('login', views.login_request, name="login"),
]