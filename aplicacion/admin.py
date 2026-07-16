from django.contrib import admin
from .models import Tabla_Pedido , Tabla_Ven , Tabla_Empleado , Tabla_Horario , Tabla_Usuario

admin.site.register(Tabla_Pedido)
admin.site.register(Tabla_Ven)
admin.site.register(Tabla_Empleado)
admin.site.register(Tabla_Horario)
admin.site.register(Tabla_Usuario)