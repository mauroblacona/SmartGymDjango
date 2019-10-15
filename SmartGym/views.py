from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import permissions, exceptions
from rest_framework import  generics
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer


class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer


class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer


class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer


class AutoridadViewSet(viewsets.ModelViewSet):
    queryset = Autoridad.objects.all()
    serializer_class = AutoridadSerializer


class PosibleClienteViewSet(viewsets.ModelViewSet):
    queryset = PosibleCliente.objects.all()
    serializer_class = PosibleClienteSerializer


class ConsultorioViewSet(viewsets.ModelViewSet):
    queryset = Consultorio.objects.all()
    serializer_class = ConsultorioSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class AsistenciaSocioViewSet(viewsets.ModelViewSet):
    queryset = AsistenciaSocio.objects.all()
    serializer_class = AsistenciaSocioSerializer


class AsistenciaEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = AsistenciaEmpleado.objects.all()
    serializer_class = AsistenciaEmpleadoSerializer


class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer


class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer


class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer


class CajaViewSet(viewsets.ModelViewSet):
    queryset = Caja.objects.all()
    serializer_class = CajaSerializer


class RecordatorioViewSet(viewsets.ModelViewSet):
    queryset = Recordatorio.objects.all()
    serializer_class = RecordatorioSerializer


class CuotaViewSet(viewsets.ModelViewSet):
    queryset = Cuota.objects.all()
    serializer_class = CuotaSerializer


class LiquidacionViewSet(viewsets.ModelViewSet):
    queryset = Liquidacion.objects.all()
    serializer_class = LiquidacionSerializer


class PagoAProveedoresViewSet(viewsets.ModelViewSet):
    queryset = PagoAProveedores.objects.all()
    serializer_class = PagoAProveedoresSerializer


class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer


class HttpResponseUnauthorized(HttpResponse):
    def __init__(self):
        self.status_code = 401

        return HttpResponseUnauthorized()
