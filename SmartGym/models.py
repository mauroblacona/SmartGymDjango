from django.db import models


class Persona(models.Model):
    nombre = models.CharField('Nombres', max_length=120)
    apellido = models.CharField('Apellidos', max_length=120)
    email = models.EmailField('Correo Electronico', max_length=200, null=True, blank=True)
    dni = models.IntegerField('Documento', null=True, blank=True)
    tel_fijo = models.CharField('Telefono Fijo', null=True, max_length=50, blank=True)
    celular = models.CharField('Celular', null=True, max_length=50, blank=True)
    domicilio = models.CharField('Domicilio', max_length=200, null=True, blank=True)

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
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=True, blank=True)
    telefono_emergencia = models.CharField('Telefono de Emergencia', null=True, blank=True, max_length=50)
    fecha_inicio = models.DateField('Fecha de Inicio', null=True, blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.apellido)


class Actividad(models.Model):
    nombre = models.CharField('Nombre', max_length=150)
    capacidad = models.IntegerField('Capacidad', blank=True, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    horarios = models.TextField('Horarios', null=True, blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return self.nombre


class Socio(Persona):
    ficha_medica = models.TextField('Ficha Medica', null=True, blank=True)
    foto = models.ImageField('Foto de Perfil', null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=True, blank=True)
    telefono_emergencia = models.CharField('Telefono de Emergencia', null=True, blank=True, max_length=50)
    fecha_inicio = models.DateField('Fecha de Inicio', null=True, blank=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True, blank=True)
    saldo = models.BooleanField('Al dia / Debe', default=True, null=True, blank=True)
    observaciones_medicas = models.TextField('Observaciones Medicas', blank=True, null=True)

    class Meta:
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'

    def __str__(self):
        return '{0} - {0}'.format(self.nombre, self.apellido)


class Profesional(Persona):
    fecha_inicio = models.DateField('Fecha de Inicio', null=True, blank=True)
    profesion = models.CharField('Profesion', max_length=70, blank=True)
    matricula = models.CharField('Matricula', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return '{0},{1}'.format(self.nombre, self.apellido)


class Autoridad(Persona):
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=True, blank=True)
    telefono_emergencia = models.CharField('Telefono de Emergencia', null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = 'Autoridad'
        verbose_name_plural = 'Autoridades'

    def __str__(self):
        return '{0},{1}'.format(self.nombre, self.apellido)


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
            return '{} - {}'.format(self.nombre, self.apellido)


class Consultorio(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField('Nombre', max_length=120, null=True, blank=True)
    fecha = models.DateField('Fecha Inicio', null=True, blank=True)
    duracion_contrato = models.TextField('Duracion del Contrato', null=True, blank=True)
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

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre


class AsistenciaSocio(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    fecha_ingreso = models.DateTimeField('Fecha de Ingreso', null=True, blank=True)
    hora_ingreso = models.DateTimeField('Hora de Ingreso', null=True, blank=True)

    class Meta:
        verbose_name = 'Asistencia Socio'
        verbose_name_plural = 'Asistencias Socios'


class AsistenciaEmpleado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    fecha_ingreso = models.DateTimeField('Fecha de Ingreso', null=True, blank=True)
    hora_ingreso = models.DateTimeField('Hora de Ingreso', null=True, blank=True)

    class Meta:
        verbose_name = 'Asistencia Empleado'
        verbose_name_plural = 'Asistencias Empleados'


class Insumo(models.Model):
    nombre = models.CharField('Nombre', max_length=120, null=True, blank=True)
    estado = models.IntegerField(choices=[('E', 'Excelente'),
                                        ('B', 'Bueno'),
                                        ('M', 'Malo'),
                                        ('R', 'En Reparacion')], null=True, blank=True)
    observacion = models.TextField('Observaciones', null=True, blank=True)

    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'

    def __str__(self):
        return'{} - {}'.format(self.nombre, self.estado)


class Ejercicio(models.Model):
    nombre = models.CharField('Nombre', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'

    def __str__(self):
        return self.nombre


class Rutina(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField('Nombre', max_length=50, null=True, blank=True)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, null=True, blank=True)
    duracion = models.CharField('Duracion de la Rutina', max_length=50, null=True, blank=True)
    tipo = models.CharField('Tipo de Rutina', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Rutina'
        verbose_name_plural = 'Rutinas'

    def __str__(self):
        return'{} - {}'.format(self.nombre, self.socio)


class Turno(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateTimeField('Fecha del Turno', null=True, blank=True)
    es_fijo = models.BooleanField(default=True, null=True, blank=True)


class Caja(models.Model):
    tipo = models.IntegerField(choices=[('I', 'Ingreso'),
                                        ('E', 'Egreso')])
    descripcion = models.TextField('Descripcion', null=True, blank=True)


class Recordatorio(models.Model):
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, null=True, blank=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    fecha = models.DateTimeField('Fecha del Recordatorio', null=True, blank=True)


class Cuota(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateTimeField('Fecha del Recordatorio', null=True, blank=True)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    monto = models.IntegerField('Monto', null=True, blank=True)
    metodo = models.CharField('Metodo de Pago', max_length=50, null=True, blank=True)


class Liquidacion(models.Model):
    fecha = models.DateTimeField('Fecha del Recordatorio', null=True, blank=True)


class PagoAProveedores(models.Model):
    fecha = models.DateTimeField('Fecha del Recordatorio', null=True, blank=True)
