from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id', 'nombre', 'direccion', 'telefono')


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'nombre', 'apellido', 'email', 'dni', 'tel_fijo', 'celular', 'domicilio',
                  'foto', 'fecha_nacimiento', 'telefono_emergencia', 'fecha_inicio', 'sucursal')


class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socio
        fields = ('id', 'nombre', 'apellido', 'email', 'dni', 'tel_fijo', 'celular', 'domicilio',
                  'ficha_medica', 'foto', 'fecha_nacimiento', 'telefono_emergencia', 'fecha_inicio', 'actividad',
                  'saldo', 'observaciones_medicas')


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ('id', 'nombre', 'capacidad', 'empleado', 'precio', 'horarios',
                  'sucursal')


class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = ('id', 'nombre', 'apellido', 'email', 'dni', 'tel_fijo', 'celular', 'domicilio',
                  'fecha_inicio', 'profesion', 'matricula')


class AutoridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autoridad
        fields = ('id', 'nombre', 'apellido', 'email', 'dni', 'tel_fijo', 'celular', 'domicilio',
                  'fecha_nacimiento', 'telefono_emergencia')


class PosibleClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosibleCliente
        fields = ('id', 'nombre', 'apellido', 'email', 'fecha_consulta', 'actividad')


class ConsultorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultorio
        fields = ('id', 'profesional', 'nombre', 'fecha', 'duracion_contrato', 'horarios', 'sucursal')


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id', 'fecha_inicio', 'cuit', 'nombre', 'telefono', 'correo', 'rubro', 'domicilio')


class AsistenciaEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsistenciaEmpleado
        fields = ('id', 'empleado', 'fecha_inicio', 'hora_ingeso')


class AsistenciaSocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsistenciaSocio
        fields = ('id', 'socio', 'fecha_inicio', 'hora_ingreso')


class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ('id', 'nombre', 'estado', 'observaciones')


class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = ('id', 'socio', 'nombre', 'ejercicio', 'duracion', 'tipo')


class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = ('id', 'nombre')


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ('id', 'socio', 'actividad', 'fecha', 'es_fijo')


class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ('id', 'tipo', 'descripcion')


class RecordatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recordatorio
        fields = ('id', 'titulo', 'socio', 'descripcion', 'fecha')


class CuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuota
        fields = ('id', 'socio', 'fecha', 'descripcion', 'monto', 'metodo')


class LiquidacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liquidacion
        fields = ('id', 'fecha')


class PagoAProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagoAProveedores
        fields = ('id', 'fecha')


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ('id', 'hora_inicio', 'hora_fin', 'dia', 'actividad')