"""SmartGymDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from SmartGym import views

router = routers.DefaultRouter()
router.register(r'empleados', views.EmpleadoViewSet)
router.register(r'socios', views.SocioViewSet)
router.register(r'sucursales', views.SucursalViewSet)
router.register(r'actividades', views.ActividadViewSet)
router.register(r'profesionales', views.ProfesionalViewSet)
router.register(r'autoridades', views.AutoridadViewSet)
router.register(r'posiblesclientes', views.PosibleClienteViewSet)
router.register(r'consultorios', views.ConsultorioViewSet)
router.register(r'proveedores', views.ProveedorViewSet)
router.register(r'asistenciasocios', views.AsistenciaSocioViewSet)
router.register(r'asistenciaempleados', views.AsistenciaEmpleadoViewSet)
router.register(r'insumos', views.InsumoViewSet)
router.register(r'ejercicios', views.EjercicioViewSet)
router.register(r'rutinas', views.RutinaViewSet)
router.register(r'turnos', views.TurnoViewSet)
router.register(r'cajas', views.CajaViewSet)
router.register(r'recordatorios', views.RecordatorioViewSet)
router.register(r'cuotas', views.CuotaViewSet)
router.register(r'liquidaciones', views.LiquidacionViewSet)
router.register(r'horarios', views.HorarioViewSet)
router.register(r'usuarios', views.UserViewSet)


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view()),
    path('principal/', views.principal, name='principal')
]

admin.site.site_header = 'SmartGym'
admin.site.index_title = 'SmartGym'
admin.site.site_title = 'Panel Administrativo'
