from django.contrib import admin
from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Home, name="home"),
    path('about/', views.About, name="about"),
    #--LOGIN--
    path('accounts/login', views.login_request, name="login"),
    path('loguot', LogoutView.as_view(template_name='AppCoder/logout.html'), name="logout"),
    #Registro USER
    path('accounts/signup', views.register_request, name="registro"),
    path('editarPerfil/', views.editarPerfil, name="editarPerfil"),
    #CARGA
    path('FormularioPerfil/', views.formularioPerfil, name="FormularioPerfil"),
    #CRUD
    path('pages/', views.PerfilesList.as_view(), name="Perfiles_lista"),
    path('detallesPerfiles/<pk>', views.PerfilesDetail.as_view(), name="Perfiles_detalles"),
    path('perfiles/editar/<pk>', views.PerfilesUpdate.as_view(), name="Perfiles_editar"),
    path('perfiles/borrar/<pk>', views.PerfilesDelete.as_view(), name="Perfiles_borrar"),
]