from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=25, default='Nombre Desconocido')  # Proporcionar un valor por defecto
    descripcion = models.TextField(max_length=250,default='Sin descripción')  # Proporcionar un valor por defecto
    cantidad = models.IntegerField(default=0)  # Proporcionar un valor por defecto
    precio = models.IntegerField(default=0)  # Proporcionar un valor por defecto
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class ProductoAprobado(models.Model):
    nombre_producto_aprobado = models.CharField(max_length=255)
    estado_producto_aprobado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_producto_aprobado