from django.db import models

class Tabla_Pedido(models.Model):
    Id_Pedido = models.CharField()
    Nombre_Pedido = models.CharField()
    Categoria_Pedido = models.CharField()
    Mesa_Pedido = models.CharField()
    Fecha_Pedido = models.DateField()
    Hora_Pedido = models.TimeField()

    def __str__(self):
        return f"{self.Id_Pedido} - {self.Nombre_Pedido}"

class Tabla_Ven(models.Model):
    Id_Ventas = models.CharField()
    Nombre_Ventas = models.CharField()
    Mesa_Ventas = models.CharField()
    Monto_Ventas = models.CharField()
    Metodo_Ventas = models.CharField()
    Fecha_Ventas = models.DateField()
    Hora_Ventas = models.TimeField()

    def __str__(self):
        return f"{self.Id_Ventas} - {self.Nombre_Ventas}"
    
class Tabla_Empleado(models.Model):
    Id_Empleado = models.CharField()
    Nombre_Empleado = models.CharField()
    Cargo_Empleado = models.CharField()
    Numero_Empleado = models.CharField()
    Ubicacion_Empleado = models.CharField()
    Correo_Empleado = models.CharField()
    Tiempo_Contrato_Empleado = models.CharField()

    def __str__(self):
        return f"{self.Id_Empleado} - {self.Nombre_Empleado}"
    

class Tabla_Horario(models.Model):
    Id_Horario = models.CharField()
    Nombre_Horario = models.CharField()
    Fecha_Horario = models.DateField()
    Hora_Inicio_Horario = models.TimeField()
    Hora_Final_Horario = models.TimeField()
    Comentario_Horario = models.CharField()

    def __str__(self):
        return f"{self.Id_Horario} - {self.Nombre_Horario}"
    
class Tabla_Usuario(models.Model):
    Id_Usuario = models.CharField()
    Nombre_Usuario = models.CharField()
    Contrasenia_Usuario = models.CharField()
    Fecha_Creacion_Usuario = models.DateField()
    Hora_Creacion_Usuario = models.TimeField()
    Comentario_Usuario = models.CharField()

    def __str__(self):
        return f"{self.Id_Usuario} - {self.Nombre_Usuario}"
    