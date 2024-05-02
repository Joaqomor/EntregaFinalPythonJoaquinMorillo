from django.contrib import admin

from .models import Producto, Cliente,Sucursal, Avatar

# Register your models here.

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Sucursal)
admin.site.register(Avatar)