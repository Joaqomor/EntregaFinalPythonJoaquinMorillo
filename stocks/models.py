from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    email = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.telefono} - {self.email} - {self.localidad} - "


class Producto(models.Model):
    
    CATEGORIAS_OPCIONES = (
        ('Electro', 'Electrodomésticos'),
        ('Ropa', 'Ropa'),
        ('Alimentos', 'Alimentos'),
        ('Juguetes', 'Juguetes'),
        ('Bebidas', 'Bebidas'),
        
    )
    nombre_de_producto = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_OPCIONES)
    precio = models.CharField(max_length=20)
    codigo = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.nombre_de_producto} - {self.categoria} - {self.precio} - {self.codigo} - {self.descripcion} - "
    
class Sucursal(models.Model):
    
    CATEGORIAS_OPCIONES = (
        ('Hipermercado', 'Hipermercado'),
        ('Supermercado', 'Supermercado'),
        ('Maximercado', 'Maximercado'),
        ('Minimercado', 'Minimercado'),
        
    )
    tipo_de_sucursal = models.CharField(max_length=20, choices=CATEGORIAS_OPCIONES)
    tamaño = models.CharField(max_length=20)
    localidad = models.CharField(max_length=20)
    cantidad_de_empleados = models.CharField(max_length=20)
    
    
    def __str__(self):
        return f"{self.tipo_de_sucursal} - {self.tamaño} - {self.localidad} - {self.cantidad_de_empleados} -  "
    
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')
    image = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return f"Avatar for {self.user.username}"