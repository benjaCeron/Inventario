from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Proveedor
# from .forms import ProveedorForm # type: ignore
import json
from django.http import JsonResponse
from django.conf import settings


def read_json_view(request):
    file_path = settings.JSON_FILE_PATH
    with open(file_path, 'r') as file:
        data = json.load(file)
    return JsonResponse(data)

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
    context = {}
    if request.method == "POST":
        id_producto = obtener_ultimo_id() + 1  # Obtener el próximo ID disponible
        nombre = request.POST["nombre_producto"].capitalize()
        descripcion = request.POST["descripcion_producto"].capitalize()
        cantidad = int(request.POST["cantidad_producto"])  # Convertir a entero
        precio = int(request.POST["precio_producto"])  # Convertir a entero

        # Crear un nuevo diccionario para el nuevo producto
        nuevo_producto = {
            "id_producto": id_producto,
            "nombre_producto": nombre,
            "descripcion_producto": descripcion,
            "cantidad_producto": cantidad,
            "precio_producto": precio
        }

        # Leer el archivo JSON
        with open('Data/data.json', 'r') as archivo:
            datos = json.load(archivo)

        # Obtener la lista de productos del diccionario o crearla si no existe
        productos_json = datos.get('productos', [])

        # Agregar el nuevo producto a la lista de productos
        productos_json.append(nuevo_producto)

        # Actualizar el diccionario con la lista de productos modificada
        datos['productos'] = productos_json

        # Escribir el diccionario actualizado de nuevo al archivo JSON
        with open('Data/data.json', 'w') as archivo:
            json.dump(datos, archivo, indent=4)

        context['mensaje'] = "OK, Producto Agregado..."

    return render(request, 'productos/ProductosAdd.html', context)

def obtener_ultimo_id():
    try:
        with open('Data/data.json', 'r') as archivo:
            datos = json.load(archivo)
            productos = datos.get('productos', [])  # Obtener la lista de productos del diccionario

            if productos:  # Verificar si hay productos en la lista
                ultimo_producto = productos[-1]  # Obtener el último producto de la lista
                return ultimo_producto.get('id_producto', 0)  # Obtener el ID del último producto
            else:
                return 0  # Si no hay productos, devolver 0 como el último ID
    except FileNotFoundError:
        return 0  # Si el archivo no existe, devolver 0 como el último ID

#---------------------------------Listar productos-------------------------------------------
def ProductosList(request):
    file_path = settings.JSON_FILE_PATH
    with open(file_path, 'r') as file:
        data = json.load(file)
    context = {'productos': data['productos']}
    return render(request, 'productos/ProductosList.html', context)

#---------------------------------Eliminar productos-----------------------------------------
def ConfirmarElim(request, pk):
    context = {}
    try:
        with open(settings.JSON_FILE_PATH, 'r') as file:
            data = json.load(file)

        productos = data.get('productos', [])
        producto = next((prod for prod in productos if prod['id_producto'] == pk), None)

        if producto:
            productos.remove(producto)
            data['productos'] = productos
            with open(settings.JSON_FILE_PATH, 'w') as file:
                json.dump(data, file, indent=4)

            context['mensaje'] = "Bien, el producto fue eliminado..."
        else:
            context['mensaje'] = "Error, el producto no existe..."

        context['productos'] = productos
        return redirect('ProductosList')  # Redirige a la lista de productos
    except Exception as e:
        context['mensaje'] = f"Error al eliminar el producto: {e}"
        return render(request, 'productos/ProductosList.html', context)
    
def ProductosElim(request, pk):
    try:
        with open(settings.JSON_FILE_PATH, 'r') as file:
            data = json.load(file)

        productos = data.get('productos', [])
        producto = next((prod for prod in productos if prod['id_producto'] == pk), None)

        if producto:
            mensaje = "El producto fue eliminado exitosamente."
            context = {'producto': producto, 'mensaje': mensaje}
            return render(request, 'productos/ProductosElim.html', context)
        else:
            mensaje = "Error: el ID del producto no existe."
            context = {'mensaje': mensaje}
            return render(request, 'productos/ProductosElim.html', context)
    except Exception as e:
        mensaje = f"Error: {str(e)}"
        context = {'mensaje': mensaje}
        return render(request, 'productos/ProductosElim.html', context)

#---------------------------------Modificar productos-----------------------------------------
def ProductosMod(request, pk):
    try:
        # Leer los datos del archivo JSON
        with open(settings.JSON_FILE_PATH, 'r') as file:
            data = json.load(file)

        # Buscar el producto por su ID en los datos del archivo JSON
        productos = data.get('productos', [])
        producto = next((prod for prod in productos if prod['id_producto'] == int(pk)), None)

        if producto:
            if request.method == 'POST':
                # Procesar los datos enviados en el formulario de actualización
                producto['nombre_producto'] = request.POST.get('nombre_producto', producto['nombre_producto']).capitalize()
                producto['descripcion_producto'] = request.POST.get('descripcion_producto', producto['descripcion_producto']).capitalize()
                producto['cantidad_producto'] = request.POST.get('cantidad_producto', producto['cantidad_producto'])
                producto['precio_producto'] = request.POST.get('precio_producto', producto['precio_producto'])

                # Escribir los datos actualizados de vuelta al archivo JSON
                with open(settings.JSON_FILE_PATH, 'w') as file:
                    json.dump(data, file, indent=4)

                mensaje = "Producto actualizado exitosamente."
                context = {'producto': producto, 'mensaje': mensaje}
                return render(request, 'productos/ProductosMod.html', context)
            else:
                context = {'producto': producto}
                return render(request, 'productos/ProductosMod.html', context)
        else:
            mensaje = "Error: el ID del producto no existe."
            context = {'mensaje': mensaje}
            return render(request, 'productos/ProductosMod.html', context)
    except Exception as e:
        mensaje = f"Error: {str(e)}"
        context = {'mensaje': mensaje}
        return render(request, 'productos/ProductosMod.html', context)



def ProductosUpdate(request):
     if request.method == "POST":
         idproducto=request.POST["id_producto"]
         nombre=request.POST["nombre_producto"]
         descripcion=request.POST["descripcion_producto"]
         cantidad=request.POST["cantidad_producto"]
         precio=request.POST["precio_producto"]

         producto = producto()
        
         producto.id_producto=idproducto
         producto.nombre_producto=nombre
         producto.descripcion_producto=descripcion
         producto.stock_producto=cantidad
         producto.precio_producto=precio
         producto.save()

         context = {'mensaje': "Ok, datos actualizados..."}
         return render(request, 'ProductosMod.html', context)
     else:
         productos = producto.objects.all()
         context = {'productos': productos}
         return render(request,  'productos/ProductosList.html', context)

#----------------------------------Detalle Producto------------------------------------------
def ProductosDet(request, pk):
    try:
        with open(settings.JSON_FILE_PATH, 'r') as file:
            data = json.load(file)

        productos = data.get('productos', [])
        producto = next((prod for prod in productos if prod['id_producto'] == pk), None)

        if producto:
            mensaje = "El producto fue encontrado exitosamente."
            context = {'producto': producto, 'mensaje': mensaje}
            return render(request, 'productos/ProductosDet.html', context)
        else:
            mensaje = "Error: el ID del producto no existe."
            context = {'mensaje': mensaje}
            return render(request, 'productos/ProductosDet.html', context)
    except Exception as e:
        mensaje = f"Error: {str(e)}"
        context = {'mensaje': mensaje}
        return render(request, 'productos/ProductosDet.html', context)
    

#----------------------------------Sección Proveedores-----------------------------------------

#----------------------------------Agregar Proveedores-----------------------------------------
# def proveedorList(request):
#     proveedores = proveedores.objects.all()
#     return render(request, 'proveedores/proveedorList.html', {'proveedores': proveedores})


# #----------------------------------Detalle Proveedor------------------------------------------
# def proveedorDet(request, pk):
#     proveedor = get_object_or_404(proveedor, pk=pk)
#     return render(request, 'proveedores/proveedorDet.html', {'proveedor': proveedor})

# #----------------------------------Agregar Proveedor------------------------------------------
# def proveedorAdd(request):
#     if request.method == "POST":
#         form = ProveedorForm(request.POST)
#         if form.is_valid():
#             proveedor = form.save()
#             return redirect('proveedor_detail', pk=proveedor.pk)
#     else:
#         form = ProveedorForm()
#     return render(request, 'proveedores/proveedorAdd.html', {'form': form})

# #----------------------------------Modificar Proveedor------------------------------------------
# def proveedorMod(request, pk):
#     proveedor = get_object_or_404(proveedor, pk=pk)
#     if request.method == "POST":
#         form = ProveedorForm(request.POST, instance=proveedor)
#         if form.is_valid():
#             proveedor = form.save()
#             return redirect('proveedor_detail', pk=proveedor.pk)
#     else:
#         form = ProveedorForm(instance=proveedor)
#     return render(request, 'proveedores/proveedorMod.html', {'form': form})

# #----------------------------------Eliminar Proveedor------------------------------------------
# def proveedorElim(request, pk):
#     proveedor = get_object_or_404(proveedor, pk=pk)
#     if request.method == "POST":
#         proveedor.delete()
#         return redirect('proveedor_list')
#     return render(request, 'proveedores/proveedorElim.html', {'proveedor': proveedor})