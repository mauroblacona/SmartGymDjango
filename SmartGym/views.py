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
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all().order_by('id')
    serializer_class = EmpleadoSerializer


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all().order_by('id')
    serializer_class = SucursalSerializer


class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all().order_by('id')
    serializer_class = SocioSerializer


class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all().order_by('id')
    serializer_class = ActividadSerializer


class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all().order_by('id')
    serializer_class = ProfesionalSerializer


class AutoridadViewSet(viewsets.ModelViewSet):
    queryset = Autoridad.objects.all().order_by('id')
    serializer_class = AutoridadSerializer


class PosibleClienteViewSet(viewsets.ModelViewSet):
    queryset = PosibleCliente.objects.all().order_by('id')
    serializer_class = PosibleClienteSerializer


class ConsultorioViewSet(viewsets.ModelViewSet):
    queryset = Consultorio.objects.all().order_by('id')
    serializer_class = ConsultorioSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all().order_by('id')
    serializer_class = ProveedorSerializer


class AsistenciaSocioViewSet(viewsets.ModelViewSet):
    queryset = AsistenciaSocio.objects.all().order_by('id')
    serializer_class = AsistenciaSocioSerializer


class AsistenciaEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = AsistenciaEmpleado.objects.all().order_by('id')
    serializer_class = AsistenciaEmpleadoSerializer


class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all().order_by('id')
    serializer_class = InsumoSerializer


class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all().order_by('id')
    serializer_class = EjercicioSerializer


class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all().order_by('id')
    serializer_class = RutinaSerializer


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all().order_by('id')
    serializer_class = TurnoSerializer


class CajaViewSet(viewsets.ModelViewSet):
    queryset = Caja.objects.all().order_by('id')
    serializer_class = CajaSerializer


class RecordatorioViewSet(viewsets.ModelViewSet):
    queryset = Recordatorio.objects.all().order_by('id')
    serializer_class = RecordatorioSerializer


class CuotaViewSet(viewsets.ModelViewSet):
    queryset = Cuota.objects.all().order_by('id')
    serializer_class = CuotaSerializer


class LiquidacionViewSet(viewsets.ModelViewSet):
    queryset = Liquidacion.objects.all().order_by('id')
    serializer_class = LiquidacionSerializer


class PagoAProveedoresViewSet(viewsets.ModelViewSet):
    queryset = PagoAProveedores.objects.all().order_by('id')
    serializer_class = PagoAProveedoresSerializer


class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all().order_by('id')
    serializer_class = HorarioSerializer


class HttpResponseUnauthorized(HttpResponse):
    def __init__(self):
        self.status_code = 401

        return HttpResponseUnauthorized()
