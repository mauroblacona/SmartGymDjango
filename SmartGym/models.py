from django.db import models
from django.contrib import admin
from model_utils import Choices
from django.utils.html import mark_safe
from auditlog.registry import auditlog


class Persona(models.Model):
    nombre = models.CharField('Nombres', max_length=120, null=True, blank=True)
    apellido = models.CharField('Apellidos', max_length=120, null=True, blank=True)
    email = models.EmailField('Correo Electronico', max_length=200, null=True, blank=True)
    dni = models.IntegerField('Documento', null=True, blank=True)
    GENEROS = Choices('Indefinido', 'Masculino', 'Femenino')
    genero = models.CharField('Genero', null=True, max_length=50, blank=True, choices=GENEROS)
    telefono = models.CharField('Telefono', null=True, max_length=50, blank=True)
    telefono_emergencia = models.CharField('Telefono de Emergencia', null=True, max_length=50, blank=True)
    domicilio = models.CharField('Domicilio', max_length=200, null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=True, blank=True)
    fecha_inicio = models.DateField('Fecha de Inicio', null=True, blank=True)
    foto = models.ImageField('Foto de Perfil', null=True, blank=True, upload_to='imagenes/')

    class Meta:
        abstract = True


class Sucursal(models.Model):
    nombre = models.CharField('Nombre', max_length=120)
    direccion = models.CharField('Direccion', null=True, max_length=50)
    telefono = models.CharField('Telefono', null=True, max_length=50)
    encargado = models.CharField('Encargado', null=True, max_length=50)

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'

    def __str__(self):
        return self.nombre


class SucursalAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'direccion')
    list_display = ('nombre', 'direccion', 'telefono', 'encargado')
    #list_filter = ('genero', 'saldo', 'actividades', 'fecha_inicio')
    #readonly_fields = ["foto_perfil"]


class Empleado(Persona):
    ficha_medica = models.ImageField('Ficha Medica', null=True, blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)
    especialidad = models.CharField('Especialidad', max_length=200, null=True, blank=True)
    observaciones_medicas = models.TextField('Observaciones Medicas', blank=True, null=True)
    actividades = models.ManyToManyField('Actividad', blank=True)
    ACTIVO, INACTIVO = ('AC', 'IN')
    STATUSES = ((ACTIVO, 'Activo'), (INACTIVO, 'Inactivo'),)
    status = models.CharField(choices=STATUSES, null=True, blank=True, max_length=150)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return '{0} - {1}'.format(self.nombre, self.apellido)


class EmpleadoAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'dni', 'apellido')
    list_display = ('nombre', 'apellido', 'dni', 'email', 'especialidad', 'status')
    list_filter = ('genero', 'especialidad', 'actividades', 'fecha_inicio', 'status')
    #readonly_fields = ["foto_perfil"]

    def marcar_inactivo(self, request, queryset):
        count = queryset.update(status=Empleado.INACTIVO)
        self.message_user(request, '{} empleados inactivos.'.format(count))
    marcar_inactivo.short_description = "Marcar los seleccionados como Inactivos"


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
        return '{0} - {1}'.format(self.nombre, self.sucursal)


class ActividadAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'sucursal__nombre')
    list_display = ('nombre', 'capacidad', 'precio', 'sucursal')
    list_filter = ('capacidad', 'precio', 'sucursal')
    #readonly_fields = ["foto_perfil"]


class Horario(models.Model):
    hora_inicio = models.CharField('Hora de Inicio', null=True, blank=True, max_length=150)
    hora_fin = models.CharField('Hora de Fin', null=True, blank=True, max_length=150)
    DIAS = Choices('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')
    dia = models.CharField('Dia de la Actividad', null=True, blank=True, choices=DIAS, max_length=150)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios de las Actividades'

    def __str__(self):
        return '{} - {}'.format(self.actividad, self.empleado)


class HorarioAdmin(admin.ModelAdmin):
    search_fields = ('actividad__nombre', 'dia')
    list_display = ('hora_inicio', 'hora_fin', 'dia', 'actividad', 'empleado')
    list_filter = ('dia', 'actividad', 'empleado')
    #readonly_fields = ["foto_perfil"]


class Socio(Persona):
    ficha_medica = models.ImageField('Ficha Medica', null=True, blank=True, upload_to="imagenes")
    actividades = models.ManyToManyField('Actividad', blank=True)
    saldo = models.BooleanField('Al dia / Debe', default=True, null=True, blank=True)
    observaciones_medicas = models.TextField('Observaciones Medicas', blank=True, null=True)
    ACTIVO, INACTIVO= ('AC', 'IN')
    STATUSES = ((ACTIVO, 'Activo'), (INACTIVO, 'Inactivo'),)
    status = models.CharField(choices=STATUSES, null=True, blank=True, max_length=150)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)
    cuenta = models.IntegerField('Cuenta', blank=True, null=True)

    class Meta:
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'

    def __str__(self):
        return '{0} - {1}'.format(self.nombre, self.apellido)

    def foto_perfil(self):
        return mark_safe('<img src="/media/%s" width="200" height="200"/>' % self.foto)

    foto_perfil.short_description = 'Foto de Perfil'


class SocioAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'dni', 'apellido')
    list_display = ('nombre', 'apellido', 'dni', 'email', 'saldo', 'status', 'cuenta')
    list_filter = ('genero', 'saldo', 'actividades', 'fecha_inicio', 'status')
    readonly_fields = ["foto_perfil"]
    actions = ['marcar_inactivo', ]

    def marcar_inactivo(self, request, queryset):
        count = queryset.update(status=Socio.INACTIVO)
        self.message_user(request, '{} socios inactivos.'.format(count))
    marcar_inactivo.short_description = "Marcar los seleccionados como Inactivos"


class Profesional(Persona):
    profesion = models.CharField('Profesion', max_length=70, blank=True, null=True)
    matricula = models.CharField('Matricula', max_length=50, null=True, blank=True)
    fecha_desde = models.DateField('Fecha Desde', blank=True, null=True)
    fecha_hasta = models.DateField('Fecha Hasta', blank=True, null=True)
    consultorios = models.ManyToManyField('Consultorio', blank=True, through='ProfesionalXConsultorios')
    ACTIVO, INACTIVO = ('AC', 'IN')
    STATUSES = ((ACTIVO, 'Activo'), (INACTIVO, 'Inactivo'),)
    status = models.CharField(choices=STATUSES, null=True, blank=True, max_length=150)

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return '{0} - {1}'.format(self.nombre, self.apellido)


class ProfesionalAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'dni', 'apellido', 'profesion')
    list_display = ('nombre', 'apellido', 'dni', 'email', 'profesion', 'matricula', 'status')
    list_filter = ('genero', 'profesion', 'status')
    actions = ['marcar_inactivo', ]

    def marcar_inactivo(self, request, queryset):
        count = queryset.update(status=Profesional.INACTIVO)
        self.message_user(request, '{} profesionales inactivos.'.format(count))
    marcar_inactivo.short_description = "Marcar los seleccionados como Inactivos"


class Autoridad(Persona):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Autoridad'
        verbose_name_plural = 'Autoridades'

    def __str__(self):
        return '{0} - {1}'.format(self.nombre, self.apellido)


class AutoridadAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'dni', 'apellido', 'sucursal__nombre')
    list_display = ('nombre', 'apellido', 'dni', 'email', 'sucursal')
    list_filter = ('genero', 'sucursal')


class PosibleCliente(models.Model):
    nombre = models.CharField('Nombre', max_length=120, null=True, blank=True)
    apellido = models.CharField('Apellido', max_length=150, null=True)
    email = models.EmailField('Correo Electronico', blank=True, null=True)
    fecha_consulta = models.DateField('Fecha de Consulta', null=True, blank=True)
    actividad = models.TextField('Actividad Consultada', null=True, blank=True)

    class Meta:
        verbose_name = 'Posible Cliente'
        verbose_name_plural = 'Registro de Posibles Clientes'

    def __str__(self):
        return '{0} - {1}'.format(self.nombre, self.apellido)


class PosibleClienteAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'apellido')
    list_display = ('nombre', 'apellido', 'fecha_consulta', 'email', 'actividad')
    list_filter = ('actividad', 'fecha_consulta')


class Consultorio(models.Model):
    nombre = models.CharField('Nombre', max_length=120, null=True, blank=True)
    fecha_apertura = models.DateField('Fecha Apertura', null=True, blank=True)
    horarios = models.ManyToManyField('HorarioConsultorio',  blank=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Consultorio'
        verbose_name_plural = 'Consultorios'

    def __str__(self):
        return self.nombre


class ConsultorioAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'sucursal__nombre')
    list_display = ('nombre', 'fecha_apertura', 'sucursal')
    list_filter = ('sucursal', 'fecha_apertura')


class Proveedor(models.Model):
    nombre = models.CharField('Nombre', max_length=120, null=True, blank=True)
    telefono = models.CharField('Telefono de Contacto', max_length=150, null=True, blank=True)
    correo = models.EmailField('Email', null=True, blank=True)
    domicilio = models.CharField('Domicilio', max_length=100, null=True, blank=True)
    rubro = models.CharField('Rubro', max_length=120, null=True, blank=True)
    fecha_inicio = models.DateField('Fecha de Inicio', null=True, blank=True)
    cuit = models.CharField('Cuit', null=True, blank=True, max_length=50)
    monto = models.DecimalField('Monto', blank=True, null=True, max_digits=8, decimal_places=2)
    #SALDO = Choices('Al dia', 'Deuda', 'Indefinido')
    saldo = models.BooleanField('Al dia / Deuda', default=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre


class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'rubro')
    list_display = ('nombre', 'telefono', 'rubro', 'correo', 'cuit', 'monto', 'saldo')
    list_filter = ('fecha_inicio', 'rubro', 'saldo')


class AsistenciaSocio(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    fecha_ingreso = models.CharField('Fecha de Ingreso', null=True, blank=True, max_length=150)
    hora_ingreso = models.CharField('Hora de Ingreso', null=True, blank=True, max_length=150)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Asistencia Socio'
        verbose_name_plural = 'Asistencias Socios'


class AsistenciaEmpleado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    fecha_ingreso = models.CharField('Fecha de Ingreso', null=True, blank=True, max_length=150)
    hora_ingreso = models.CharField('Hora de Ingreso', null=True, blank=True, max_length=150)
    TIPO_INGRESOS = Choices('Entrada', 'Salida')
    tipo = models.BooleanField(choices=TIPO_INGRESOS, null=True, blank=True)

    class Meta:
        verbose_name = 'Asistencia Empleado'
        verbose_name_plural = 'Asistencias Empleados'

    def __str__(self):
        return self.empleado


class Insumo(models.Model):
    nombre = models.CharField('Nombre', max_length=120, null=True, blank=True)
    DISPONIBLE, NO_DISPONIBLE, A_REPARAR = ('DIS', 'NO', 'REP')
    STATUSES = ((DISPONIBLE, 'Disponible'), (NO_DISPONIBLE, 'No Disponible'), (A_REPARAR, 'A Reparar'))
    estado = models.CharField(choices=STATUSES, null=True, blank=True, max_length=150)
    observacion = models.TextField('Observaciones', null=True, blank=True)
    codigo_insumo = models.CharField('Codigo del Insumo', null=True, blank=True, max_length=100)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'

    def __str__(self):
        return'{0} - {1}'.format(self.nombre, self.codigo_insumo)


class InsumoAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'codigo_insumo')
    list_display = ('nombre', 'estado', 'codigo_insumo', 'proveedor', 'observacion')
    list_filter = ('estado', 'proveedor')
    actions = ['marcar_nodisponible', ]

    def marcar_nodisponible(self, request, queryset):
        count = queryset.update(estado=Insumo.NO_DISPONIBLE)
        self.message_user(request, '{} insumos no disponibles.'.format(count))
    marcar_nodisponible.short_description = "Marcar los seleccionados como No Disponibles"


class Ejercicio(models.Model):
    nombre = models.CharField('Nombre', max_length=200, null=True, blank=True)
    GRUPOS = Choices('Piernas', 'Hombros', 'Biceps', 'Triceps', 'Pecho', 'Espalda', 'Core', 'Otro')
    grupo_muscular = models.CharField('Grupo Muscular', max_length=200, null=True, blank=True, choices=GRUPOS)

    class Meta:
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'

    def __str__(self):
        return self.nombre


class EjercicioAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'grupo_muscular')
    list_display = ('nombre', 'grupo_muscular')
    list_filter = ('grupo_muscular', 'nombre')


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


class RutinaAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'socio__nombre')
    list_display = ('nombre', 'socio', 'duracion', 'cantidad_dias')
    #list_filter = ('genero', 'saldo', 'actividades', 'fecha_inicio')


class Turno(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True, blank=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, null=True, blank=True)
    es_fijo = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'

    def __str__(self):
        return '{0} - {1}'.format(self.socio, self.es_fijo)


class TurnoAdmin(admin.ModelAdmin):
    search_fields = ('socio__nombre', 'actividad__nombre')
    list_display = ('socio', 'actividad', 'horario', 'es_fijo')
    list_filter = ('es_fijo', 'actividad')


class Recordatorio(models.Model):
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, null=True, blank=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    fecha = models.DateTimeField('Fecha del Recordatorio', null=True, blank=True)

    class Meta:
        verbose_name = 'Recordatorio'
        verbose_name_plural = 'Recordatorios'

    def __str__(self):
        return self.socio


class RecordatorioAdmin(admin.ModelAdmin):
    search_fields = ('socio__nombre', 'fecha')
    list_display = ('turno', 'socio', 'fecha', 'descripcion')
    list_filter = ('fecha', 'socio')
    # readonly_fields = ["foto_perfil"]


class Cuota(models.Model):
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    fecha_vencimiento = models.CharField('Fecha del Vencimiento', null=True, blank=True, max_length=200)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    monto = models.IntegerField('Monto', null=True, blank=True)
    METODOS = Choices('Efectivo', 'Debito', 'Credito', 'Otro')
    metodo_pago = models.CharField('Metodo de Pago', max_length=50, null=True, blank=True, choices=METODOS)
    codigo_transaccion = models.CharField('Codigo de la transaccion', max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'Cuota'
        verbose_name_plural = 'Control de Cuotas'

    def __str__(self):
        return '{0} - {1}'.format(self.socio, self.monto)


class CuotaAdmin(admin.ModelAdmin):
    search_fields = ('socio__nombre', 'codigo_transaccion')
    list_display = ('socio', 'monto', 'fecha_vencimiento', 'metodo_pago', 'codigo_transaccion')
    list_filter = ('fecha_vencimiento', 'socio__nombre', 'metodo_pago')


class Caja(models.Model):
    TIPOS = Choices('Ingreso', 'Egreso')
    tipo = models.CharField(choices=TIPOS, max_length=150)
    MOTIVOS = Choices('Pago a Proveedores', 'Cobro Cuota', 'Otro')
    motivo = models.CharField(choices=MOTIVOS, blank=True, null=True, max_length=50)
    cuota = models.ForeignKey(Cuota, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Registro de Cajas'

    def __str__(self):
        return self.tipo


class CajaAdmin(admin.ModelAdmin):
    search_fields = ('tipo', 'motivo')
    list_display = ('tipo', 'motivo')
    list_filter = ('tipo', 'motivo')


class Liquidacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    cantidad_horas = models.IntegerField('Cantidad de Horas Liquidadas', null=True, blank=True)
    precio_hora = models.IntegerField('Precio Hora Liquidada', null=True, blank=True)
    monto_total = models.DecimalField('Total Liquidado', null=True, blank=True, max_digits=8, decimal_places=2)
    fecha = models.DateField('Fecha de la liquidacion', null=True, blank=True)

    class Meta:
        verbose_name = 'Liquidacion'
        verbose_name_plural = 'Liquidaciones de Empleados'

    def __str__(self):
        return '{0} - {1}'.format(self.empleado, self.fecha)


class LiquidacionAdmin(admin.ModelAdmin):
    search_fields = ('empleado__nombre', 'monto_total')
    list_display = ('empleado', 'cantidad_horas', 'monto_total', 'fecha')
    list_filter = ('fecha', 'monto_total')


class HorarioConsultorio(models.Model):
    hora_inicio = models.CharField('Hora de Inicio', null=True, blank=True, max_length=150)
    hora_fin = models.CharField('Hora de Fin', null=True, blank=True, max_length=150)
    DIAS = Choices('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')
    dia = models.CharField('Dia de Atención', null=True, blank=True, choices=DIAS, max_length=150)
    profesionales = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=True, blank=True)
    consultorios = models.ForeignKey(Consultorio, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Horario del Consultorio'
        verbose_name_plural = 'Horarios de los Consultorios'

    def __str__(self):
        return self.dia


class HorarioConsultorioAdmin(admin.ModelAdmin):
    search_fields = ('dia', 'profesionales__nombre', 'consultorios__nombre')
    list_display = ('dia', 'hora_inicio', 'hora_fin')
    list_filter = ('dia', 'hora_inicio')


class ProfesionalXConsultorios(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=True, blank=True)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE, null=True, blank=True)
    dia = models.DateField('Dia', blank=True, null=True)
    hora_inicio = models.DateTimeField('Hora Inicio', null=True, blank=True)
    hora_fin = models.DateTimeField('Hora Fin', null=True, blank=True)


class RutinaXEjercicio(models.Model):
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, null=True, blank=True)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, null=True, blank=True)
    peso = models.DecimalField('Peso', null=True, blank=True, max_digits=1000, decimal_places=5)
    repeticiones = models.IntegerField('Repeticiones', null=True, blank=True)
    series = models.IntegerField('Series', null=True, blank=True)


auditlog.register(Actividad)
