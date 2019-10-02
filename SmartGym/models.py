from django.db import models


class Persona(models.Model):
    nombre = models.CharField('Nombres', max_length=120)
    apellido = models.CharField('Apellidos', max_length=120)
    email = models.EmailField('Correo Electronico', max_length=200, null=True)
    dni = models.IntegerField('Documento')
    tel_fijo = models.CharField('Telefono Fijo', null=True, max_length=50)
    celular = models.CharField('Celular', null=True, max_length=50)
    domicilio = models.CharField('Domicilio', max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {}".format(self.nombre, self.apellido, self.dni, self.tel_fijo, self.email, self.celular, self.domicilio)


class Sucursal(models.Model):
    nombre = models.CharField('Nombre', max_length=120)
    direccion = models.CharField('Direccion', null=True, max_length=50)
    telefono = models.CharField('Telefono', null=True, max_length=50)

    def __str__(self):
        return "{} - {} - {}".format(self.nombre, self.direccion, self.telefono)


class Empleado(Persona):
    foto = models.ImageField('Foto de Perfil', null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento')
    telefono_emergencia = models.CharField('Telefono de Emergencia', null=True, blank=True, max_length=50)
    fecha_inicio = models.DateField('Fecha de Inicio')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.apellido)


class Actividad(models.Model):
    nombre = models.CharField('Nombre', max_length=150)
    capacidad = models.IntegerField('Capacidad', blank=True, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    horarios = models.TextField('Horarios')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return self.nombre


class Socio(Persona):
    ficha_medica = models.TextField('Ficha Medica', null=True, blank=True)
    foto = models.ImageField('Foto de Perfil', null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento')
    telefono_emergencia = models.CharField('Telefono de Emergencia', null=True, blank=True, max_length=50)
    fecha_inicio = models.DateField('Fecha de Inicio')
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    saldo = models.BooleanField('Al dia / Debe', default=True)
    observaciones_medicas = models.TextField('Observaciones Medicas', blank=True, null=True)

    class Meta:
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'

    def __str__(self):
        return '{0} - {0}'.format(self.nombre, self.apellido)


class Profesional(Persona):
    fecha_inicio = models.DateField('Fecha de Inicio')
    profesion = models.CharField('Profesion', max_length=70)
    matricula = models.CharField('Matricula', max_length=50)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return '{0},{1}'.format(self.nombre, self.apellido)


class Autoridad(Persona):
    fecha_nacimiento = models.DateField('Fecha de Nacimiento')
    telefono_emergencia = models.CharField('Telefono de Emergencia', null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = 'Autoridad'
        verbose_name_plural = 'Autoridades'

    def __str__(self):
        return '{0},{1}'.format(self.nombre, self.apellido)


class PosibleCliente(models.Model):
    nombre = models.CharField('Nombre', max_length=120)
    apellido = models.CharField('Apellido', max_length=150)
    email = models.EmailField('Correo Electronico', blank=True, null=True)
    fecha_consulta = models.DateField('Fecha de Consulta')
    actividad = models.TextField('Actividad Consultada')

    class Meta:
        verbose_name = 'Posible Cliente'
        verbose_name_plural = 'Posibles Clientes'

        def __str__(self):
            return '{} - {}'.format(self.nombre, self.apellido)


class Consultorio(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=120)
    fecha = models.DateField('Fecha Inicio')
    duracion_contrato = models.TextField('Duracion del Contrato')
    horarios = models.TextField('Horarios')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Consultorio'
        verbose_name_plural = 'Consultorios'

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField('Nombre', max_length=120)
    telefono = models.CharField('Telefono de Contacto', max_length=150)
    correo = models.EmailField('Email')
    domicilio = models.CharField('Domicilio', max_length=100)
    rubro = models.CharField('Rubro', max_length=120)
    fecha_inicio = models.DateField('Fecha de Inicio')
    cuit = models.CharField('Cuit', null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre


class AsistenciaSocio(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField('Fecha de Ingreso')
    hora_ingreso = models.DateTimeField('Hora de Ingreso')

    class Meta:
        verbose_name = 'Asistencia Socio'
        verbose_name_plural = 'Asistencias Socios'


class AsistenciaEmpleado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField('Fecha de Ingreso')
    hora_ingreso = models.DateTimeField('Hora de Ingreso')

    class Meta:
        verbose_name = 'Asistencia Empleado'
        verbose_name_plural = 'Asistencias Empleados'


class Insumo(models.Model):
    nombre = models.CharField('Nombre', max_length=120)
    estado = models.IntegerField(choices=[('E', 'Excelente'),
                                        ('B', 'Bueno'),
                                        ('M', 'Malo'),
                                        ('R', 'En Reparacion')])
    observacion = models.TextField('Observaciones', null=True, blank=True)

    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'

    def __str__(self):
        return'{} - {}'.format(self.nombre, self.estado)


class Ejercicio(models.Model):
    nombre = models.CharField('Nombre', max_length=200)

    class Meta:
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'

    def __str__(self):
        return self.nombre


class Rutina(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=50)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    duracion = models.CharField('Duracion de la Rutina', max_length=50)
    tipo = models.CharField('Tipo de Rutina', max_length=50)

    class Meta:
        verbose_name = 'Rutina'
        verbose_name_plural = 'Rutinas'

    def __str__(self):
        return'{} - {}'.format(self.nombre, self.socio)


class Turno(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fecha del Turno')
    es_fijo = models.BooleanField(default=True)


class Caja(models.Model):
    tipo = models.IntegerField(choices=[('I', 'Ingreso'),
                                        ('E', 'Egreso')])
    descripcion = models.TextField('Descripcion', null=True, blank=True)


class Recordatorio(models.Model):
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    fecha = models.DateTimeField('Fecha del Recordatorio')


class Cuota(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fecha del Recordatorio')
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    monto = models.IntegerField('Monto')
    metodo = models.CharField('Metodo de Pago', max_length=50)


class Liquidacion(models.Model):
    fecha = models.DateTimeField('Fecha del Recordatorio')


class PagoAProveedores(models.Model):
    fecha = models.DateTimeField('Fecha del Recordatorio')
