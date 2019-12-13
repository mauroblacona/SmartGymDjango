from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *
from django.shortcuts import render
from django.template import loader
from .models import *
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all().order_by('id')
    serializer_class = EmpleadoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all().order_by('id')
    serializer_class = SucursalSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all().order_by('id')
    serializer_class = SocioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all().order_by('id')
    serializer_class = ActividadSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all().order_by('id')
    serializer_class = ProfesionalSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class AutoridadViewSet(viewsets.ModelViewSet):
    queryset = Autoridad.objects.all().order_by('id')
    serializer_class = AutoridadSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class PosibleClienteViewSet(viewsets.ModelViewSet):
    queryset = PosibleCliente.objects.all().order_by('id')
    serializer_class = PosibleClienteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ConsultorioViewSet(viewsets.ModelViewSet):
    queryset = Consultorio.objects.all().order_by('id')
    serializer_class = ConsultorioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all().order_by('id')
    serializer_class = ProveedorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class AsistenciaSocioViewSet(viewsets.ModelViewSet):
    queryset = AsistenciaSocio.objects.all().order_by('id')
    serializer_class = AsistenciaSocioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)


class AsistenciaEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = AsistenciaEmpleado.objects.all().order_by('id')
    serializer_class = AsistenciaEmpleadoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all().order_by('id')
    serializer_class = InsumoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all().order_by('id')
    serializer_class = EjercicioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all().order_by('id')
    serializer_class = RutinaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all().order_by('id')
    serializer_class = TurnoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CajaViewSet(viewsets.ModelViewSet):
    queryset = Caja.objects.all().order_by('id')
    serializer_class = CajaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RecordatorioViewSet(viewsets.ModelViewSet):
    queryset = Recordatorio.objects.all().order_by('id')
    serializer_class = RecordatorioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CuotaViewSet(viewsets.ModelViewSet):
    queryset = Cuota.objects.all().order_by('id')
    serializer_class = CuotaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class LiquidacionViewSet(viewsets.ModelViewSet):
    queryset = Liquidacion.objects.all().order_by('id')
    serializer_class = LiquidacionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all().order_by('id')
    serializer_class = HorarioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RutinaXEjercicio(viewsets.ModelViewSet):
    queryset = RutinaXEjercicio.objects.all().order_by('id')
    serializer_class = RutinaXEjercicioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ProfesionalXConsultorios(viewsets.ModelViewSet):
    queryset = ProfesionalXConsultorios.objects.all().order_by('id')
    serializer_class = ProfesionalXConsultorioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class HttpResponseUnauthorized(HttpResponse):
    def __init__(self):
        self.status_code = 401

        return HttpResponseUnauthorized()


def principal(request):
    return render(request, 'principal.html', {"actividades": Actividad.objects.all()})
