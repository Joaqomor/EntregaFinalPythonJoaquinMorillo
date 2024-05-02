from django import forms

from .models import Producto, Cliente, Sucursal, Avatar


class ProductoSearchForm(forms.Form):
    nombre_de_producto = forms.CharField(max_length=50, label="Ingresar nombre de un producto")
    
    
class ClienteSearchForm(forms.Form):
    localidad = forms.CharField(max_length=50, required=True, label="Ingresar Localidad")
    
class SucursalSearchForm(forms.Form):
    CATEGORIAS_OPCIONES = (
        ('Hipermercado', 'Hipermercado'),
        ('Supermercado', 'Supermercado'),
        ('Maximercado', 'Maximercado'),
        ('Minimercado', 'Minimercado'),
        
    )
    
    tipo_de_sucursal = forms.ChoiceField(label="Ingresar tipo de sucursal", choices=CATEGORIAS_OPCIONES)


class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email', 'localidad']
        labels = {
            'nombre': 'Nombre',
            'telefono': 'Telefono',
            'email': 'Email',
            'localidad': 'Localidad',
        }


class ProductoCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_de_producto', 'categoria', 'precio', 'codigo', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),  
        }
        
class SucursalCreateForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['tipo_de_sucursal', 'tamaño', 'localidad', 'cantidad_de_empleados']
        
        
        
class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']
        

    
        