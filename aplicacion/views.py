from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Tabla_Pedido , Tabla_Ven , Tabla_Empleado , Tabla_Horario , Tabla_Usuario , Tabla_Salida_Stock , Tabla_Ingreso_Stock
from django.contrib.auth.decorators import login_required
from functools import wraps

def barra_menu(request):
    return render(request , 'barra_menu.html')

def login_requerido(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Si no tiene la sesión activa, lo manda al login
        if not request.session.get('usuario_logueado'):
            return redirect('/')  # Pon aquí la ruta de tu login si es distinta
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def login_usuario_empleado(request):
    error_message = None
    if request.method == 'POST':
        usuario_ingresado = request.POST.get('usuario', '').strip()
        contrasenia_ingresada = request.POST.get('contrasenia', '').strip()

        if usuario_ingresado == 'admin' and contrasenia_ingresada == 'admin':
            # GUARDAR LA SESIÓN AL ENTRAR
            request.session['usuario_logueado'] = True
            return redirect('/panel_control_empleado/')
        else:
            error_message = "Usuario o contraseña incorrectos. Intente de nuevo."

    return render(request, 'usuario_empleado.html', {'error': error_message})

@login_requerido
def panel_control_empleado(request):
    return render(request , 'panel_control.html')

@login_requerido
def enlace_tabla_pedido(request): 
    pedido = Tabla_Pedido.objects.all()
    return render(request , 'tabla_pedidos.html' , {
        'pedido' : pedido
    })

@login_requerido
def enlace_registrar_pedido(request): 
    return render(request , 'registrar_pedido.html')

@login_requerido
def logica_registrar_pedido(request):
    Id = request.POST['TxtIdentificacion']
    Nombre = request.POST['TxtNombre']
    Categoria = request.POST['TxtCategoria']
    Mesa = request.POST['TxtMesa']
    Fecha = request.POST['TxtFecha']
    Hora = request.POST['TxtHora']

    pedido = Tabla_Pedido.objects.create(
        Id_Pedido = Id,
        Nombre_Pedido = Nombre,
        Categoria_Pedido = Categoria,
        Mesa_Pedido = Mesa,
        Fecha_Pedido = Fecha,
        Hora_Pedido = Hora
    )
    
    return redirect('/enlace_tabla_pedido/')

@login_requerido
def logica_eliminar_pedido(request , Id_Pedido):
    pedido = Tabla_Pedido.objects.get(Id_Pedido = Id_Pedido)
    pedido.delete()
    return redirect('/enlace_tabla_pedido/')

@login_requerido
def enlace_actualizar_pedido(request , Id_Pedido):
    pedido = Tabla_Pedido.objects.get(Id_Pedido = Id_Pedido)
    return render(request , 'actualizar_pedido.html' , {
        'actualizar_pedido' : pedido
    })

@login_requerido
def logica_actualizar_pedido(request): 
    Id_Pedido = request.POST['TxtIdentificacion']
    Nombre_Pedido = request.POST['TxtNombre']
    Categoria_Pedido = request.POST['TxtCategoria']
    Mesa_Pedido = request.POST['TxtMesa']
    Fecha_Pedido = request.POST['TxtFecha']
    Hora_Pedido = request.POST['TxtHora']

    pedido = Tabla_Pedido.objects.get(Id_Pedido = Id_Pedido)
    pedido.Nombre_Pedido = Nombre_Pedido
    pedido.Categoria_Pedido = Categoria_Pedido
    pedido.Mesa_Pedido = Mesa_Pedido
    pedido.Fecha_Pedido = Fecha_Pedido
    pedido.Hora_Pedido = Hora_Pedido

    pedido.save()

    return redirect('/enlace_tabla_pedido/')

@login_requerido
def enlace_tabla_ventas(request):
    ventas = Tabla_Ven.objects.all()
    return render(request , 'tabla_ventas.html' , {
        'ventas' : ventas
    })

@login_requerido
def enlace_registrar_ventas(request):
    return render(request , 'registrar_ventas.html')

@login_requerido
def logica_registrar_ventas(request):
    Id = request.POST['TxtIdentificacion']
    Nombre = request.POST['TxtNombre']
    Mesa = request.POST['TxtMesa']
    Monto = request.POST['TxtMonto']
    Metodo = request.POST['TxtMetodo']
    Fecha = request.POST['TxtFecha']
    Hora = request.POST['TxtHora']
    
    ventas = Tabla_Ven.objects.create(
        Id_Ventas = Id,
        Nombre_Ventas = Nombre,
        Mesa_Ventas = Mesa,
        Monto_Ventas = Monto,
        Metodo_Ventas = Metodo,
        Fecha_Ventas = Fecha,
        Hora_Ventas = Hora
    )

    return redirect('/enlace_tabla_ventas/')

@login_requerido
def logica_eliminar_ventas(request , Id_Ventas):
    ventas = Tabla_Ven.objects.get(Id_Ventas = Id_Ventas)
    ventas.delete()
    return redirect('/enlace_tabla_ventas/')    

@login_requerido
def enlace_actualizar_ventas(request , Id_Ventas):
    ventas = Tabla_Ven.objects.get(Id_Ventas = Id_Ventas)
    return render(request , 'actualizar_ventas.html' , {
        'actualizar_ventas' : ventas
    })

@login_requerido
def logica_actualizar_ventas(request):
    Id_Ventas = request.POST['TxtIdentificacion']
    Nombre_Ventas = request.POST['TxtNombre']
    Mesa_Ventas = request.POST['TxtCategoria']
    Monto_Ventas = request.POST['TxtMesa']
    Metodo_Ventas = request.POST['TxtMetodo']
    Fecha_Ventas = request.POST['TxtFecha']
    Hora_Ventas = request.POST['TxtHora']

    ventas = Tabla_Ven.objects.get(Id_Ventas = Id_Ventas)
    ventas.Nombre_Ventas = Nombre_Ventas
    ventas.Mesa_Ventas = Mesa_Ventas
    ventas.Monto_Ventas = Monto_Ventas
    ventas.Metodo_Ventas = Metodo_Ventas
    ventas.Fecha_Ventas = Fecha_Ventas
    ventas.Hora_Ventas = Hora_Ventas

    ventas.save()

    return redirect('/enlace_tabla_ventas/')

@login_requerido
def enlace_tabla_empleado(request):
    empleado = Tabla_Empleado.objects.all()
    return render(request , 'tabla_empleado.html' , {
        'empleado' : empleado
    })

@login_requerido 
def enlace_registrar_empleado(request):
    return render(request , 'registrar_empleado.html')

@login_requerido
def logica_registrar_empleado(request): 
    Id = request.POST['TxtIdentificacion']
    Nombre = request.POST['TxtNombre']
    Cargo = request.POST['TxtCargo']
    Numero = request.POST['TxtTelefonico']
    Ubicacion = request.POST['TxtUbicacion']
    Correo = request.POST['TxtCorreo']
    Tiempo_Contrato = request.POST['TxtContrato']

    empleado = Tabla_Empleado.objects.create(
        Id_Empleado = Id,
        Nombre_Empleado = Nombre,
        Cargo_Empleado = Cargo,
        Numero_Empleado = Numero,
        Ubicacion_Empleado = Ubicacion,
        Correo_Empleado = Correo,
        Tiempo_Contrato_Empleado = Tiempo_Contrato
    )

    return redirect('/enlace_tabla_empleado/')

@login_requerido
def logica_eliminar_empleado(request , Id_Empleado):
    empleado = Tabla_Empleado.objects.get(Id_Empleado = Id_Empleado)
    empleado.delete()
    return redirect('/enlace_tabla_empleado/')

@login_requerido
def enlace_actualizar_empleado(request , Id_Empleado):
    empleado = Tabla_Empleado.objects.get(Id_Empleado = Id_Empleado)
    return render(request , "actualizar_empleado.html" , {
        'actualizar_empleado' : empleado
    })

@login_requerido
def logica_actualizar_empleado(request): 
    Id_Empleado = request.POST['TxtIdentificacion']
    Nombre_Empleado = request.POST['TxtNombre']
    Cargo_Empleado = request.POST['TxtCargo']
    Numero_Empleado = request.POST['TxtTelefonico']
    Ubicacion_Empleado = request.POST['TxtUbicacion']
    Correo_Empleado = request.POST['TxtCorreo']
    Tiempo_Contrato_Empleado = request.POST['TxtContrato']

    empleado = Tabla_Empleado.objects.get(Id_Empleado = Id_Empleado)
    empleado.Nombre_Empleado = Nombre_Empleado
    empleado.Cargo_Empleado = Cargo_Empleado
    empleado.Numero_Empleado = Numero_Empleado
    empleado.Ubicacion_Empleado = Ubicacion_Empleado
    empleado.Correo_Empleado = Correo_Empleado
    empleado.Tiempo_Contrato_Empleado = Tiempo_Contrato_Empleado

    empleado.save()

    return redirect('/enlace_tabla_empleado/')

@login_requerido
def enlace_tabla_horario(request):
    horario = Tabla_Horario.objects.all()
    return render(request , "tabla_horario.html" , {
        'horario' : horario
    })

@login_requerido
def enlace_registrar_horario(request):
    return render(request , "registrar_horario.html")

@login_requerido
def logica_registrar_horario(request):
    Id = request.POST['TxtIdentificacion']
    Nombre = request.POST['TxtNombre']
    Fecha = request.POST['TxtFecha']
    Hora_Inicio = request.POST['TxtHoraInicio']
    Hora_Final = request.POST['TxtHoraFinal']
    Comentario = request.POST['TxtComentario']
    
    horario = Tabla_Horario.objects.create(
        Id_Horario = Id,
        Nombre_Horario = Nombre,
        Fecha_Horario = Fecha,
        Hora_Inicio_Horario = Hora_Inicio,
        Hora_Final_Horario = Hora_Final,
        Comentario_Horario = Comentario
    )

    return redirect('/enlace_tabla_horario/')

@login_requerido
def logica_eliminar_horario(request , Id_Horario): 
    horario = Tabla_Horario.objects.get(Id_Horario = Id_Horario)
    horario.delete()
    return redirect('/enlace_tabla_horario/')

@login_requerido
def enlace_actualiza_horario(request , Id_Horario): 
    horario = Tabla_Horario.objects.get(Id_Horario = Id_Horario)
    return render(request , 'actualizar_horario.html' , {
        'actualizar_horario' : horario
    })

@login_requerido
def logica_actualizar_horario(request):
    Id_Horario = request.POST['TxtIdentificacion']
    Nombre_Horario = request.POST['TxtNombre']
    Fecha_Horario = request.POST['TxtFecha']
    Hora_Inicio_Horario = request.POST['TxtHoraInicio']
    Hora_Final_Horario = request.POST['TxtHoraFinal']
    Comentario_Horario = request.POST['TxtComentario']

    horario = Tabla_Horario.objects.get(Id_Horario = Id_Horario)
    horario.Nombre_Horario = Nombre_Horario
    horario.Fecha_Horario = Fecha_Horario
    horario.Hora_Inicio_Horario = Hora_Inicio_Horario
    horario.Hora_Final_Horario = Hora_Final_Horario
    horario.Comentario_Horario = Comentario_Horario
    
    horario.save()

    return redirect('/enlace_tabla_horario/')

@login_requerido
def enlace_tabla_usuario(request):
    usuario = Tabla_Usuario.objects.all()
    return render(request , 'tabla_usuario.html' , {
        'usuario' : usuario
    })

@login_requerido
def enlace_registrar_usuario(request): 
    return render(request , 'registrar_usuario.html')

@login_requerido
def logica_registrar_usuario(request): 
    Id = request.POST['TxtIdentificacion']
    Nombre = request.POST['TxtNombre']
    Contrasenia = request.POST['TxtContrasenia']
    Fecha_Creacion = request.POST['TxtFecha']
    Hora_Creacion = request.POST['TxtHora']
    Comentario = request.POST['TxtComentario']
    
    horario = Tabla_Usuario.objects.create(
        Id_Usuario = Id,
        Nombre_Usuario = Nombre,
        Contrasenia_Usuario = Contrasenia,
        Fecha_Creacion_Usuario = Fecha_Creacion,
        Hora_Creacion_Usuario = Hora_Creacion,
        Comentario_Usuario = Comentario
    )
    
    return redirect('/enlace_tabla_usuario/')

@login_requerido
def logica_eliminar_usuario(request , Id_Usuario):
    usuario = Tabla_Usuario.objects.get(Id_Usuario = Id_Usuario)
    usuario.delete()
    return redirect('/enlace_tabla_usuario/')

@login_requerido
def enlace_actualizar_usuario(request , Id_Usuario):
    usuario = Tabla_Usuario.objects.get(Id_Usuario = Id_Usuario)
    return render(request , 'actualizar_usuario.html' , {
        'actualizar_usuario' : usuario
    })

@login_requerido
def logica_actualizar_usuario(request): 
    Id_Usuario = request.POST['TxtIdentificacion']
    Nombre_Usuario = request.POST['TxtNombre']
    Contrasenia_Usuario = request.POST['TxtContrasenia']
    Fecha_Creacion_Usuario = request.POST['TxtFecha']
    Hora_Creacion_Usuario = request.POST['TxtHora']
    Comentario_Usuario = request.POST['TxtComentario']

    usuario = Tabla_Usuario.objects.get(Id_Usuario = Id_Usuario)
    usuario.Nombre_Usuario = Nombre_Usuario
    usuario.Contrasenia_Usuario = Contrasenia_Usuario
    usuario.Fecha_Creacion_Usuario = Fecha_Creacion_Usuario
    usuario.Hora_Creacion_Usuario = Hora_Creacion_Usuario
    usuario.Comentario_Usuario = Comentario_Usuario

    usuario.save()

    return redirect('/enlace_tabla_usuario/')

@login_requerido
def enlace_tabla_ingresos_stock(request):
    stock = Tabla_Ingreso_Stock.objects.all()
    return render(request , "tabla_ingresos_stock.html" , {
        'stock' : stock
    })

@login_requerido
def enlace_registrar_ingresos_stock(request):
    return render(request , "registrar_ingresos_stock.html")

@login_requerido
def logica_registrar_ingresos_stock(request):
    Id = request.POST['TxtIdentificacion']
    Fecha = request.POST['TxtNombre']
    Usuario = request.POST['txtUsuario']
    Nombre = request.POST['txtNombreMaterial']
    Descripion = request.POST['txtDescripcionMaterial']
    Cantidad = request.POST['txtCantidadMaterial']

    ingreso_stock = Tabla_Ingreso_Stock.objects.create(
        Id_Ingreso_Stock = Id,
        Fecha_Ingreso_Stock = Fecha,
        Usuario_Salida_Stock = Usuario,
        Nombre_Ingreso_Stock = Nombre,
        Descripion_Ingreso_Stock = Descripion,
        Cantidad_Ingreso_Stock = Cantidad,
    )
    return redirect('/enlace_tabla_ingresos_stock/')

@login_requerido
def logica_eliminar_ingresos_stock(request , Id_Ingreso_Stock):
    ingreso_stock = Tabla_Ingreso_Stock.objects.get(Id_Ingreso_Stock = Id_Ingreso_Stock)
    ingreso_stock.delete()
    return redirect('/enlace_tabla_ingresos_stock/')

@login_requerido
def enlace_actualizar_ingresos_stock(request , Id_Ingreso_Stock):
    actualizar_ingreso_stock = Tabla_Ingreso_Stock.objects.get(Id_Ingreso_Stock = Id_Ingreso_Stock)
    return render(request , "actualizar_ingresos_stock.html" , {
        "actualizar_stock" : actualizar_ingreso_stock
    })

@login_requerido
def logica_actulizar_ingresos_stock(request): 
    Id_Ingreso_Stock = request.POST['TxtIdentificacion']
    Fecha_Ingreso_Stock = request.POST['TxtNombre']
    Usuario_Salida_Stock = request.POST['txtUsuario']
    Nombre_Ingreso_Stock = request.POST['txtNombreMaterial']
    Descripion_Ingreso_Stock = request.POST['txtDescripcionMaterial']
    Cantidad_Ingreso_Stock = request.POST['txtCantidadMaterial']

    actualizar_ingresos_stock = Tabla_Ingreso_Stock.objects.get(Id_Ingreso_Stock = Id_Ingreso_Stock)
    actualizar_ingresos_stock.Fecha_Ingreso_Stock = Fecha_Ingreso_Stock
    actualizar_ingresos_stock.Usuario_Salida_Stock = Usuario_Salida_Stock
    actualizar_ingresos_stock.Nombre_Ingreso_Stock = Nombre_Ingreso_Stock
    actualizar_ingresos_stock.Descripion_Ingreso_Stock = Descripion_Ingreso_Stock
    actualizar_ingresos_stock.Cantidad_Ingreso_Stock = Cantidad_Ingreso_Stock

    actualizar_ingresos_stock.save()

    return redirect("/enlace_tabla_ingresos_stock/")

@login_requerido
def enlace_tabla_salida_stock(request):
    salida_stock = Tabla_Salida_Stock.objects.all()
    return render(request , "tabla_salida_stock.html" , {
        'salida_stock' : salida_stock
    })

@login_requerido
def enlace_registrar_salida_stock(request):
    return render(request , "registrar_salida_stock.html")

@login_requerido
def logica_registrar_salida_stock(request): 
    Id = request.POST['TxtIdentificacion']
    Fecha = request.POST['TxtNombre']
    Usuario = request.POST['txtUsuario']
    Nombre = request.POST['txtNombreMaterial']
    Descripcion = request.POST['txtDescripcionMaterial']
    Cantidad = request.POST['txtCantidadMaterial']
    
    salida_stock = Tabla_Salida_Stock.objects.create(
        Id_Salida_Stock = Id,
        Fecha_Salida_Stock = Fecha,
        Usuario_Salida_Stock = Usuario,
        Nombre_Salida_Stock = Nombre,
        Descripcion_Salida_Stock = Descripcion,
        Cantidad_Salida_Stock = Cantidad,
    )

    return redirect('/enlace_tabla_salida_stock/')

@login_requerido
def logica_eliminar_salida_stock(request , Id_Salida_Stock):
    salida_stock = Tabla_Salida_Stock.objects.get(Id_Salida_Stock = Id_Salida_Stock)
    salida_stock.delete()
    return redirect('/enlace_tabla_salida_stock/')

@login_requerido
def enlace_actualizar_salida_stock(request , Id_Salida_Stock):
    actualizar_salida_stock = Tabla_Salida_Stock.objects.get(Id_Salida_Stock = Id_Salida_Stock)
    return render(request , "actualizar_salida_stock.html" , {
        "actualizar_salida_stock" :  actualizar_salida_stock
    })

@login_requerido
def logica_actualizar_salida_stock(request):
    Id_Salida_Stock = request.POST['TxtIdentificacion']
    Fecha_Salida_Stock = request.POST['TxtNombre']
    Usuario_Salida_Stock = request.POST['txtUsuario']
    Nombre_Salida_Stock = request.POST['txtNombreMaterial']
    Descripcion_Salida_Stock = request.POST['txtDescripcionMaterial']
    Cantidad_Salida_Stock = request.POST['txtCantidadMaterial']

    actualizar_salida_stock = Tabla_Salida_Stock.objects.get(Id_Salida_Stock = Id_Salida_Stock)
    actualizar_salida_stock.Fecha_Salida_Stock = Fecha_Salida_Stock
    actualizar_salida_stock.Usuario_Salida_Stock = Usuario_Salida_Stock
    actualizar_salida_stock.Nombre_Salida_Stock = Nombre_Salida_Stock
    actualizar_salida_stock.Descripcion_Salida_Stock = Descripcion_Salida_Stock
    actualizar_salida_stock.Cantidad_Salida_Stock = Cantidad_Salida_Stock

    actualizar_salida_stock.save()

    return redirect('/enlace_tabla_salida_stock/')

