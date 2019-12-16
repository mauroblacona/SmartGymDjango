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
        fields = ('id', 'nombre', 'direccion', 'telefono', 'encargado')


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'nombre', 'apellido', 'email', 'dni', 'genero', 'telefono', 'telefono_emergencia',
                  'domicilio', 'fecha_nacimiento', 'fecha_inicio', 'sucursal', 'foto', 'ficha_medica', 'status',
                  'especialidad', 'observaciones_medicas', 'actividades')


class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socio
        fields = ('id', 'nombre', 'apellido', 'email', 'dni', 'genero', 'telefono', 'telefono_emergencia',
                  'domicilio', 'fecha_nacimiento', 'fecha_inicio', 'foto', 'ficha_medica', 'actividades'
                  , 'saldo', 'observaciones_medicas', 'status', 'sucursal', 'cuenta')


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ('id', 'nombre', 'capacidad', 'empleados', 'sucursal', 'precio')


class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = ('id', 'nombre', 'apellido', 'email', 'dni', 'genero', 'telefono', 'telefono_emergencia',
                  'domicilio', 'fecha_nacimiento', 'fecha_inicio', 'sucursal', 'foto', 'profesion',
                  'matricula', 'fecha_desde', 'fecha_hasta', 'consultorios', 'status')


class AutoridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autoridad
        fields = ('id', 'nombre', 'apellido', 'email', 'dni', 'genero', 'telefono', 'telefono_emergencia',
                  'domicilio', 'fecha_nacimiento', 'fecha_inicio', 'sucursal', 'foto')


class PosibleClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosibleCliente
        fields = ('id', 'nombre', 'apellido', 'email', 'fecha_consulta', 'actividad')


class ConsultorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultorio
        fields = ('id', 'nombre', 'fecha_apertura', 'horarios', 'sucursal')


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id', 'fecha_inicio', 'cuit', 'nombre', 'telefono', 'correo', 'rubro', 'domicilio', 'saldo', 'monto')


class AsistenciaEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsistenciaEmpleado
        fields = ('id', 'empleado', 'fecha_ingreso', 'hora_ingreso', 'tipo')


class AsistenciaSocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsistenciaSocio
        fields = ('id', 'socio', 'fecha_ingreso', 'hora_ingreso', 'sucursal')


class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ('id', 'nombre', 'estado', 'observacion', 'codigo_insumo', 'proveedor')


class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = ('id', 'socio', 'nombre', 'ejercicio', 'duracion', 'cantidad_dias', 'descripcion')


class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = ('id', 'nombre', 'grupo_muscular')


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ('id', 'socio', 'actividad', 'horario', 'es_fijo')


class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = ('id', 'tipo', 'motivo', 'metodo_pago')


class RecordatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recordatorio
        fields = ('id', 'turno', 'socio', 'descripcion', 'fecha')


class CuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuota
        fields = ('id', 'socio', 'fecha_vencimiento', 'descripcion', 'monto', 'metodo_pago', 'codigo_transaccion')


class LiquidacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liquidacion
        fields = ('id', 'empleado', 'cantidad_horas', 'precio_hora', 'monto_total', 'fecha')


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ('id', 'hora_inicio', 'hora_fin', 'dia', 'actividad', 'empleado')


class ProfesionalXConsultorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfesionalXConsultorios
        fields = ('id', 'profesional', 'consultorio', 'dia', 'hora_inicio', 'hora_fin')


class RutinaXEjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutinaXEjercicio
        fields = ('id', 'rutina', 'ejercicio', 'peso', 'repeticiones', 'series')
