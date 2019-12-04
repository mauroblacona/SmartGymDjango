from django.db import models
from django.contrib import admin




class Persona(models.Model):
    nombre = models.CharField('Nombres', max_length=120, null=True, blank=True)
    apellido = models.CharField('Apellidos', max_length=120, null=True, blank=True)
    email = models.EmailField('Correo Electronico', max_length=200, null=True, blank=True)
    dni = models.IntegerField('Documento', null=True, blank=True)
    genero = models.CharField('Genero', null=True, max_length=50, blank=True)
    telefono = models.CharField('Telefono', null=True, max_length=50, blank=True)
    telefono_emergencia = models.CharField('Telefono de Emergencia', null=True, max_length=50, blank=True)
    domicilio = models.CharField('Domicilio', max_length=200, null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=True, blank=True)
    fecha_inicio = models.DateField('Fecha de Inicio', null=True, blank=True)
    foto = models.ImageField('Foto de Perfil', null=True, blank=True)

    class Meta:
        abstract = True


class Sucursal(models.Model):
    nombre = models.CharField('Nombre', max_length=120)
    direccion = models.CharField('Direccion', null=True, max_length=50)
    telefono = models.CharField('Telefono', null=True, max_length=50)

    def __str__(self):
        return self.nombre


class Empleado(Persona):
    ficha_medica = models.ImageField('Ficha Medica', null=True, blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)
    especialidad = models.CharField('Especialidad', max_length=200, null=True, blank=True)
    observaciones_medicas = models.TextField('Observaciones Medicas', blank=True, null=True)
    actividades = models.ManyToManyField('Actividad', blank=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.apellido)


class Actividad(models.Model):
    nombre = models.CharField('Nombre', max_length=150)
    capacidad = models.IntegerField('Capacidad', blank=True, null=True)
    empleados = models.ManyToManyField('Empleado', blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)
    precio = models.IntegerField('Precio', null=True, blank=True)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return self.nombre


class Horario(models.Model):
    hora_inicio = models.DateTimeField('Hora de Inicio', null=True, blank=True)
    hora_fin = models.DateTimeField('Hora de Fin', null=True, blank=True)
    dia = models.DateField('Dia de la Actividad', null=True, blank=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return self.actividad


class Socio(Persona):
    ficha_medica = models.TextField('Ficha Medica', null=True, blank=True)
    actividades = models.ManyToManyField('Actividad', blank=True)
    saldo = models.BooleanField('Al dia / Debe', default=True, null=True, blank=True)
    observaciones_medicas = models.TextField('Observaciones Medicas', blank=True, null=True)



    class Meta:
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'


    def __str__(self):
        return '{0} - {1}'.format(self.nombre, self.apellido)


class SocioAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'dni')
    list_display = ('nombre', 'apellido', 'dni', 'email', 'telefono_emergencia')
    list_filter = ('genero', 'saldo')


class Profesional(Persona):
    profesion = models.CharField('Profesion', max_length=70, blank=True, null=True)
    matricula = models.CharField('Matricula', max_length=50, null=True, blank=True)
    fecha_desde = models.DateField('Fecha Desde', blank=True, null=True)
    fecha_hasta = models.DateField('Fecha Hasta', blank=True, null=True)
    consultorios = models.ManyToManyField('Consultorio', blank=True, through='ProfesionalXConsultorios')

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return '{0} - {1}'.format(self.nombre, self.apellido)


class Autoridad(Persona):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Autoridad'
        verbose_name_plural = 'Autoridades'

    def __str__(self):
        return '{0} - {1}'.format(self.nombre, self.apellido)


class PosibleCliente(models.Model):
    nombre = models.CharField('Nombre', max_length=120, null=True, blank=True)
    apellido = models.CharField('Apellido', max_length=150, null=True)
    email = models.EmailField('Correo Electronico', blank=True, null=True)
    fecha_consulta = models.DateField('Fecha de Consulta', null=True, blank=True)
    actividad = models.TextField('Actividad Consultada', null=True, blank=True)

    class Meta:
        verbose_name = 'Posible Cliente'
        verbose_name_plural = 'Posibles Clientes'

        def __str__(self):
            return '{0} - {1}'.format(self.nombre, self.apellido)


class Consultorio(models.Model):
    nombre = models.CharField('Nombre', max_length=120, null=True, blank=True)
    fecha_apertura = models.DateField('Fecha Apertura', null=True, blank=True)
    horarios = models.TextField('Horarios', null=True, blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Consultorio'
        verbose_name_plural = 'Consultorios'

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField('Nombre', max_length=120, null=True, blank=True)
    telefono = models.CharField('Telefono de Contacto', max_length=150, null=True, blank=True)
    correo = models.EmailField('Email', null=True, blank=True)
    domicilio = models.CharField('Domicilio', max_length=100, null=True, blank=True)
    rubro = models.CharField('Rubro', max_length=120, null=True, blank=True)
    fecha_inicio = models.DateField('Fecha de Inicio', null=True, blank=True)
    cuit = models.CharField('Cuit', null=True, blank=True, max_length=50)
    saldo = models.DecimalField(choices=[
                                        ('Al dia', 'Al dia'),
                                        ('Debe', 'Debe')], null=True, blank=True, max_digits=10, decimal_places=10)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre


class AsistenciaSocio(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    fecha_ingreso = models.DateTimeField('Fecha de Ingreso', null=True, blank=True)
    hora_ingreso = models.DateTimeField('Hora de Ingreso', null=True, blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Asistencia Socio'
        verbose_name_plural = 'Asistencias Socios'


class AsistenciaEmpleado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    fecha_ingreso = models.DateTimeField('Fecha de Ingreso', null=True, blank=True)
    hora_ingreso = models.DateTimeField('Hora de Ingreso', null=True, blank=True)
    tipo = models.BooleanField(choices=[('E', 'Entrada'),
                                        ('S', 'Salida')], null=True, blank=True)

    class Meta:
        verbose_name = 'Asistencia Empleado'
        verbose_name_plural = 'Asistencias Empleados'


class Insumo(models.Model):
    nombre = models.CharField('Nombre', max_length=120, null=True, blank=True)
    estado = models.IntegerField(choices=[
                                        ('B', 'Bueno'),
                                        ('M', 'Malo'),
                                        ('R', 'En Reparacion')], null=True, blank=True)
    observacion = models.TextField('Observaciones', null=True, blank=True)
    codigo_insumo = models.CharField('Codigo del Insumo', null=True, blank=True, max_length=100)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'

    def __str__(self):
        return'{0} - {1}'.format(self.nombre, self.estado)


class Ejercicio(models.Model):
    nombre = models.CharField('Nombre', max_length=200, null=True, blank=True)
    musculo = models.CharField('Musculo', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'

    def __str__(self):
        return self.nombre


class Rutina(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField('Nombre', max_length=50, null=True, blank=True)
    ejercicio = models.ManyToManyField('Ejercicio', blank=True, through='RutinaXEjercicio')
    duracion = models.CharField('Duracion de la Rutina', max_length=50, null=True, blank=True)
    cantidad_dias = models.IntegerField('Cantidad de Dias Semanales', null=True, blank=True)
    descripcion = models.TextField('Descripcion', null=True, blank=True)

    class Meta:
        verbose_name = 'Rutina'
        verbose_name_plural = 'Rutinas'

    def __str__(self):
        return '{0} - {1}'.format(self.nombre, self.socio)


class Turno(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True, blank=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, null=True, blank=True)
    es_fijo = models.BooleanField(default=True, null=True, blank=True)


class Caja(models.Model):
    tipo = models.IntegerField(choices=[('I', 'Ingreso'),
                                        ('E', 'Egreso')])
    motivo = models.CharField(choices=[('Pago', 'Pago a Proveedores'),
                                        ('Cobro', 'Cobro Cuota')], blank=True, null=True, max_length=50)
    metodo_pago = models.CharField('Metodo de Pago', max_length=50, null=True, blank=True)


class Recordatorio(models.Model):
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, null=True, blank=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    fecha = models.DateTimeField('Fecha del Recordatorio', null=True, blank=True)


class Cuota(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    fecha_vencimiento = models.DateTimeField('Fecha del Vencimiento', null=True, blank=True)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    monto = models.IntegerField('Monto', null=True, blank=True)


class Liquidacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    cantidad_horas = models.IntegerField('Cantidad de Horas Liquidadas', null=True, blank=True)
    precio_hora = models.IntegerField('Precio Hora Liquidada', null=True, blank=True)
    monto_total = models.DecimalField('Total Liquidado', null=True, blank=True, max_digits=10, decimal_places=10)
    fecha = models.DateField('Fecha de la liquidacion', null=True, blank=True)


class ProfesionalXConsultorios(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=True, blank=True)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE, null=True, blank=True)
    dia = models.DateField('Dia', blank=True, null=True)
    hora_inicio = models.DateTimeField('Hora Inicio', null=True, blank=True)
    hora_fin = models.DateTimeField('Hora Fin', null=True, blank=True)


class RutinaXEjercicio(models.Model):
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, null=True, blank=True)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, null=True, blank=True)
    peso = models.DecimalField('Peso', null=True, blank=True, max_digits=10, decimal_places=10)
    repeticiones = models.IntegerField('Repeticiones', null=True, blank=True)
    series = models.IntegerField('Repeticiones', null=True, blank=True)
