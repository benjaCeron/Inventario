from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.Home,name='Home'),

#-----------------------------Usuarios---------------------------------------------
    path('Login', views.Login,name='Login'),
    path('Perfil', views.Perfil,name='Perfil'),
#----------------------------------------------------------------------------------

#-----------------------------Productos--------------------------------------------
    path('ProductosAdd', views.ProductosAdd,name='ProductosAdd'),
    path('ProductosList', views.ProductosList,name='ProductosList'),
    path('ProductosElim', views.ProductosElim,name='ProductosElim'),
    path('ProductosDet', views.ProductosDet,name='ProductosDet'),
    path('ProductosMod', views.ProductosMod,name='ProductosMod'),
#----------------------------------------------------------------------------------


]