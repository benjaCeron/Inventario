from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


#----------------------------------Inicio de Página------------------------------------------
def Home(request):
    return render(request,'Home.html')

def Perfil(request):
    return render(request,'Usuario\Perfil.html')

#----------------------------------Inicio de sesion------------------------------------------

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email-login')
        password = request.POST.get('contrasenia-login')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            Login(request, user)
            return redirect('Home.html')
        else:
            context = {'mensaje': "Error de autenticación"}
            return render(request, 'Home.html', context)
    else:
        
        return render(request, 'Usuario\Login.html')


#----------------------------------Sección Productos-----------------------------------------

#----------------------------------Agregar Producto------------------------------------------
def ProductosAdd(request):
    # if request.method != "POST":
    #     productos=Producto.objects.all()
    #     context = {'productos':productos}
    #     return render(request,'ProductosAdd.html', context)
    # else:
    #     idproducto=request.POST["id_producto"]
    #     nombre=request.POST["nombre_producto"]
    #     descripcion=request.POST["descripcion_producto"]
    #     cantidad=request.POST["cantidad_producto"]
    #     precio=request.POST["precio_producto"]
    #     obj = Producto.objects.create(id_producto = idproducto,
    #                                   nombre_producto = nombre,
    #                                   descripcion_producto = descripcion,
    #                                   stock_producto = cantidad,
    #                                   precio_producto = precio)
        
    #     obj.save()
    #     context = {'mensaje': "OK, datos grabados..."}
    #     return render(request,'ProductosAdd.html', context)
    return render(request,'Productos\ProductosAdd.html')

#---------------------------------Listar productos-------------------------------------------
def ProductosList(request):
    # productos = Producto.objects.all()
    # context = {'productos': productos}
    # return render(request, 'Listar_productos.html', context)
    return render(request,'Productos\ProductosList.html')

#---------------------------------Eliminar productos-----------------------------------------
def ProductosElim(request):
    # ,pk
    # context={}
    # try:
    #     producto = Producto.objects.get(id_producto=pk)

    #     producto.delete()
    #     mensaje = "Bien, el producto fue eliminado..."
    #     productos = {'productos': productos, 'mensaje':mensaje}
    #     return render (request, 'Listar_productos.html', context)
    # except:
    #     mensaje = " Error, id no existe..."
    #     productos = Producto.objects.all()
    #     context = {'productos': productos, 'mensaje':mensaje}
    #     return render( request, 'Listar_productos.html', context)
    return render(request,'Productos\ProductosElim.html')


def ProductosMod(request):
    # , pk
    # if pk != "":
    #     producto = get_object_or_404(Producto, id_producto=pk)
    #     if request.method == 'POST':
    #         # Procesar los datos enviados en el formulario de actualización
    #         producto.nombre_producto = request.POST.get('nombre_producto', '')
    #         producto.descripcion_producto = request.POST.get('descripcion_producto', '')
    #         producto.stock_producto = request.POST.get('cantidad_producto', '')
    #         producto.precio_producto = request.POST.get('precio_producto', '')
    #         producto.save()
    #         mensaje = "Producto actualizado exitosamente."
    #         context = {'producto': producto, 'mensaje': mensaje}
    #     else:
    #         context = {'producto': producto}
    #     return render(request, 'ProductosMod.html', context)
    # else:
    #     context = {'mensaje': "Error, ID vacío..."}
    #     return render(request, 'ProductosMod.html', context)
    return render(request,'Productos\ProductosMod.html')


# def ProductosUpdate(request):
#     if request.method == "POST":
#         idproducto=request.POST["id_producto"]
#         nombre=request.POST["nombre_producto"]
#         descripcion=request.POST["descripcion_producto"]
#         cantidad=request.POST["cantidad_producto"]
#         precio=request.POST["precio_producto"]

#         producto = Producto()
        
#         producto.id_producto=idproducto
#         producto.nombre_producto=nombre
#         producto.descripcion_producto=descripcion
#         producto.stock_producto=cantidad
#         producto.precio_producto=precio
#         producto.save()

#         context = {'mensaje': "Ok, datos actualizados..."}
#         return render(request, 'ProductosMod.html', context)
#     else:
#         productos = Producto.objects.all()
#         context = {'productos': productos}
#         return render(request,  'Listar_productos.html', context)

#----------------------------------Detalle Producto------------------------------------------
def ProductosDet(request):
    # if request.method != "POST":
    #     productos=Producto.objects.all()
    #     context = {'productos':productos}
    #     return render(request,'ProductosAdd.html', context)
    # else:
    #     idproducto=request.POST["id_producto"]
    #     nombre=request.POST["nombre_producto"]
    #     descripcion=request.POST["descripcion_producto"]
    #     cantidad=request.POST["cantidad_producto"]
    #     precio=request.POST["precio_producto"]
    #     obj = Producto.objects.create(id_producto = idproducto,
    #                                   nombre_producto = nombre,
    #                                   descripcion_producto = descripcion,
    #                                   stock_producto = cantidad,
    #                                   precio_producto = precio)
        
    #     obj.save()
    #     context = {'mensaje': "OK, datos grabados..."}
    #     return render(request,'ProductosAdd.html', context)
    return render(request,'Productos\ProductosDet.html')