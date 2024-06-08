from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from . import views
from .views import read_json_view

urlpatterns = [

    path('read-json/', read_json_view, name='read_json'),
    path('admin/', admin.site.urls),
    path('', views.Home,name='Home'),

#-----------------------------Usuarios---------------------------------------------
    path('Login', views.Login,name='Login'),
    path('Perfil', views.Perfil,name='Perfil'),
#----------------------------------------------------------------------------------

#-----------------------------Productos--------------------------------------------
    path('ProductosAdd', views.ProductosAdd,name='ProductosAdd'),
    path('ProductosList/', views.ProductosList,name='ProductosList'),
    path('ProductosElim/<int:pk>/', views.ProductosElim,name='ProductosElim'),
    path('ConfirmElimar/<int:pk>/', views.ConfirmarElim,name='ConfirmarElim'),
    path('ProductosDet/<int:pk>/', views.ProductosDet,name='ProductosDet'),
    path('ProductosMod/<int:pk>/', views.ProductosMod,name='ProductosMod'),
    path('ProductosUpdate',views.ProductosUpdate, name='ProductosUpdate'),
#----------------------------------------------------------------------------------

#-----------------------------Proveedores------------------------------------------
    # path('ProveedorAdd', views.proveedorAdd,name='ProveedorAdd'),
    # path('ProveedorList', views.proveedorList,name='ProveedorList'),
    # path('ProveedorElim', views.proveedorElim,name='ProveedorElim'),
    # path('ProveedorDet', views.proveedorDet,name='ProveedorDet'),
    # path('ProveedorMod', views.proveedorMod,name='ProveedorMod'),
#----------------------------------------------------------------------------------
]