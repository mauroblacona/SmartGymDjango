from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id', 'nombre', 'direccion', 'telefono')


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'nombre', 'apellido', 'email', 'dni', 'genero', 'telefono', 'telefono_emergencia',
                  'domicilio', 'fecha_nacimiento', 'fecha_inicio', 'sucursal',
                  'especialidad', 'observaciones_medicas', 'actividades')


class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socio
        fields = ('id', 'nombre', 'apellido', 'email', 'dni', 'genero', 'telefono',  'telefono_emergencia',
                  'domicilio', 'ficha_medica', 'foto', 'fecha_nacimiento', 'actividad', 'saldo',
                  'observaciones_medicas')


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ('id', 'nombre', 'capacidad', 'empleados', 'horarios', 'sucursal',
                  'precio')


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
        fields = ('id', 'empleado', 'fecha_ingreso', 'hora_ingreso')


class AsistenciaSocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsistenciaSocio
        fields = ('id', 'socio', 'fecha_ingreso', 'hora_ingreso')


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