from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import permissions, exceptions
from rest_framework import  generics
from django.http import HttpResponse
from django.shortcuts import render


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def list(self, request, *args, **kwargs):
        empleados = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleados, many=True)
        return Response(serializer.data)


class HttpResponseUnauthorized(HttpResponse):
    def __init__(self):
        self.status_code = 401

        return HttpResponseUnauthorized()
