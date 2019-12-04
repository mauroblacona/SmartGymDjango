from django.contrib import admin


from .models import *

admin.site.register(Sucursal)
admin.site.register(Empleado)
admin.site.register(Socio, SocioAdmin)
admin.site.register(Actividad)
admin.site.register(Profesional)
admin.site.register(Autoridad)
admin.site.register(PosibleCliente)
admin.site.register(Consultorio)
admin.site.register(Proveedor)
admin.site.register(AsistenciaEmpleado)
admin.site.register(AsistenciaSocio)
admin.site.register(Insumo)
admin.site.register(Rutina)
admin.site.register(Ejercicio)
admin.site.register(Turno)
admin.site.register(Recordatorio)
admin.site.register(Cuota)
admin.site.register(Caja)
admin.site.register(Liquidacion)
admin.site.register(ProfesionalXConsultorios)
admin.site.register(RutinaXEjercicio)

admin.site.site_url = "/principal/"

