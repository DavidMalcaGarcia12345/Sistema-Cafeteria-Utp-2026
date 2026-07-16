from django.urls import path
from . import views

urlpatterns = [
    path('' , views.login_usuario_empleado), 
    path('panel_control_empleado/' , views.panel_control_empleado), 
    path('enlace_tabla_pedido/' , views.enlace_tabla_pedido),
    path('enlace_registrar_pedido/' , views.enlace_registrar_pedido),
    path('logica_registrar_pedido/' , views.logica_registrar_pedido),
    path('enlace_tabla_pedido/logica_eliminar_pedido/<Id_Pedido>' , views.logica_eliminar_pedido), 
    path('enlace_tabla_pedido/enlace_actualizar_pedido/<Id_Pedido>' , views.enlace_actualizar_pedido), 
    path('logica_actualizar_pedido/' , views.logica_actualizar_pedido), 

    path('enlace_tabla_ventas/' , views.enlace_tabla_ventas), 
    path('enlace_registrar_ventas/' , views.enlace_registrar_ventas), 
    path('logica_registrar_ventas/' , views.logica_registrar_ventas),
    path('enlace_tabla_ventas/logica_eliminar_ventas/<Id_Ventas>' , views.logica_eliminar_ventas), 
    path('enlace_tabla_ventas/enlace_actualizar_ventas/<Id_Ventas>' , views.enlace_actualizar_ventas), 
    path('logica_actualizar_ventas/' , views.logica_actualizar_ventas), 

    path('enlace_tabla_empleado/' , views.enlace_tabla_empleado),
    path('enlace_registrar_empleado/' , views.enlace_registrar_empleado), 
    path('logica_registrar_empleado/' , views.logica_registrar_empleado), 
    path('enlace_tabla_empleado/logica_eliminar_empleado/<Id_Empleado>' , views.logica_eliminar_empleado), 
    path('enlace_tabla_empleado/enlace_actualizar_empleado/<Id_Empleado>' , views.enlace_actualizar_empleado), 
    path('logica_actualizar_empleado/' , views.logica_actualizar_empleado), 

    path('enlace_tabla_horario/' , views.enlace_tabla_horario), 
    path('enlace_registrar_horario/' , views.enlace_registrar_horario), 
    path('logica_registrar_horario/' , views.logica_registrar_horario), 
    path('enlace_tabla_horario/logica_eliminar_horario/<Id_Horario>' , views.logica_eliminar_horario), 
    path('enlace_tabla_horario/enlace_actualiza_horario/<Id_Horario>' , views.enlace_actualiza_horario), 
    path('logica_actualizar_horario/' , views.logica_actualizar_horario),

    path('enlace_tabla_usuario/' , views.enlace_tabla_usuario), 
    path('enlace_registrar_usuario/' , views.enlace_registrar_usuario), 
    path('logica_registrar_usuario/' , views.logica_registrar_usuario), 
    path('enlace_tabla_usuario/logica_eliminar_usuario/<Id_Usuario>' , views.logica_eliminar_usuario), 
    path('enlace_tabla_usuario/enlace_actualizar_usuario/<Id_Usuario>' , views.enlace_actualizar_usuario), 
    path('logica_actualizar_usuario/' , views.logica_actualizar_usuario)
]