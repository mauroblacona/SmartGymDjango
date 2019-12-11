from django.contrib import admin


from .models import *

admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Socio, SocioAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Profesional, ProfesionalAdmin)
admin.site.register(Autoridad, AutoridadAdmin)
admin.site.register(PosibleCliente, PosibleClienteAdmin)
admin.site.register(Consultorio, ConsultorioAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(AsistenciaEmpleado)
admin.site.register(HorarioConsultorio, HorarioConsultorioAdmin)
admin.site.register(AsistenciaSocio)
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Rutina, RutinaAdmin)
admin.site.register(Ejercicio, EjercicioAdmin)
admin.site.register(Turno, TurnoAdmin)
admin.site.register(Recordatorio, RecordatorioAdmin)
admin.site.register(Cuota, CuotaAdmin)
admin.site.register(Caja, CajaAdmin)
admin.site.register(Liquidacion, LiquidacionAdmin)
admin.site.register(ProfesionalXConsultorios)
admin.site.register(RutinaXEjercicio)

fields = ['image_tag']
readonly_fields = ['image_tag']

