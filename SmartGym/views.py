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

    # def list(self, request, *args, **kwargs):
    #      if request.method == 'GET':
    #          empleados = Empleado.objects.all()
    #          serializer = EmpleadoSerializer(empleados, many=True)
    #          return JsonResponse(serializer.data, safe=False)


    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = EmpleadoSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse(serializer.errors, status=400)
    #
    #     elif request.method == 'PUT':
    #         data = JSONParser().parse(request)
    #         serializer = SocioSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data)
    #         return JsonResponse(serializer.errors, status=400)
    #
    #     elif request.method == 'DELETE':
    #         empleados = Empleado.objects.all(pk=id)
    #         import ipdb;
    #         ipdb.set_trace()
    #         empleados.delete()
    #         return JsonResponse(status=204)


class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer

    # def list(self, request, *args, **kwargs):
    #      if request.method == 'GET':
    #          socios = Socio.objects.all()
    #          serializer = SocioSerializer(socios, many=True)
    #          return JsonResponse(serializer.data, safe=False)


    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = SocioSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse(serializer.errors, status=400)
    #
    #     elif request.method == 'PUT':
    #         data = JSONParser().parse(request)
    #         serializer = SocioSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data)
    #         return JsonResponse(serializer.errors, status=400)
    #
    #     elif request.method == 'DELETE':
    #         socios = Socio.objects.all()
    #         import ipdb; ipdb.set_trace()
    #         socios.delete()
    #         return JsonResponse(status=204)


class HttpResponseUnauthorized(HttpResponse):
    def __init__(self):
        self.status_code = 401

        return HttpResponseUnauthorized()
