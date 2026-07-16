from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Tabla_Pedido , Tabla_Ven , Tabla_Empleado , Tabla_Horario , Tabla_Usuario

def barra_menu(request):
    return render(request , 'barra_menu.html')

def login_usuario_empleado(request):
    error_message = None
    
    if request.method == 'POST':
        # Obtenemos los datos y usamos .strip() para quitar espacios vacíos accidentales
        usuario_ingresado = request.POST.get('usuario', '').strip()
        contrasenia_ingresada = request.POST.get('contrasenia', '').strip()
        
        # 1. Validamos que ninguno de los campos esté vacío
        if not usuario_ingresado or not contrasenia_ingresada:
            error_message = "Por favor, complete todos los campos."
            
        # 2. Si no están vacíos, validamos las credenciales correctas
        elif usuario_ingresado == 'empleado' and contrasenia_ingresada == '123':
            return redirect('/panel_control_empleado/')
        
        # 3. Si están llenos pero son incorrectos
        else:
            error_message = "Usuario o contraseña incorrectos. Intente de nuevo."
            
    return render(request, 'usuario_empleado.html', {'error': error_message})

def panel_control_empleado(request):
    return render(request , 'panel_control.html')

def enlace_tabla_pedido(request): 
    pedido = Tabla_Pedido.objects.all()
    return render(request , 'tabla_pedidos.html' , {
        'pedido' : pedido
    })

def enlace_registrar_pedido(request): 
    return render(request , 'registrar_pedido.html')

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

def logica_eliminar_pedido(request , Id_Pedido):
    pedido = Tabla_Pedido.objects.get(Id_Pedido = Id_Pedido)
    pedido.delete()
    return redirect('/enlace_tabla_pedido/')

def enlace_actualizar_pedido(request , Id_Pedido):
    pedido = Tabla_Pedido.objects.get(Id_Pedido = Id_Pedido)
    return render(request , 'actualizar_pedido.html' , {
        'actualizar_pedido' : pedido
    })

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

def enlace_tabla_ventas(request):
    ventas = Tabla_Ven.objects.all()
    return render(request , 'tabla_ventas.html' , {
        'ventas' : ventas
    })

def enlace_registrar_ventas(request):
    return render(request , 'registrar_ventas.html')

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

def logica_eliminar_ventas(request , Id_Ventas):
    ventas = Tabla_Ven.objects.get(Id_Ventas = Id_Ventas)
    ventas.delete()
    return redirect('/enlace_tabla_ventas/')    

def enlace_actualizar_ventas(request , Id_Ventas):
    ventas = Tabla_Ven.objects.get(Id_Ventas = Id_Ventas)
    return render(request , 'actualizar_ventas.html' , {
        'actualizar_ventas' : ventas
    })

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

def enlace_tabla_empleado(request):
    empleado = Tabla_Empleado.objects.all()
    return render(request , 'tabla_empleado.html' , {
        'empleado' : empleado
    })
    
def enlace_registrar_empleado(request):
    return render(request , 'registrar_empleado.html')

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

def logica_eliminar_empleado(request , Id_Empleado):
    empleado = Tabla_Empleado.objects.get(Id_Empleado = Id_Empleado)
    empleado.delete()
    return redirect('/enlace_tabla_empleado/')

def enlace_actualizar_empleado(request , Id_Empleado):
    empleado = Tabla_Empleado.objects.get(Id_Empleado = Id_Empleado)
    return render(request , "actualizar_empleado.html" , {
        'actualizar_empleado' : empleado
    })

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

def enlace_tabla_horario(request):
    horario = Tabla_Horario.objects.all()
    return render(request , "tabla_horario.html" , {
        'horario' : horario
    })

def enlace_registrar_horario(request):
    return render(request , "registrar_horario.html")

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


def logica_eliminar_horario(request , Id_Horario): 
    horario = Tabla_Horario.objects.get(Id_Horario = Id_Horario)
    horario.delete()
    return redirect('/enlace_tabla_horario/')

def enlace_actualiza_horario(request , Id_Horario): 
    horario = Tabla_Horario.objects.get(Id_Horario = Id_Horario)
    return render(request , 'actualizar_horario.html' , {
        'actualizar_horario' : horario
    })

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

def enlace_tabla_usuario(request):
    usuario = Tabla_Usuario.objects.all()
    return render(request , 'tabla_usuario.html' , {
        'usuario' : usuario
    })

def enlace_registrar_usuario(request): 
    return render(request , 'registrar_usuario.html')

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

def logica_eliminar_usuario(request , Id_Usuario):
    usuario = Tabla_Usuario.objects.get(Id_Usuario = Id_Usuario)
    usuario.delete()
    return redirect('/enlace_tabla_usuario/')

def enlace_actualizar_usuario(request , Id_Usuario):
    usuario = Tabla_Usuario.objects.get(Id_Usuario = Id_Usuario)
    return render(request , 'actualizar_usuario.html' , {
        'actualizar_usuario' : usuario
    })

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