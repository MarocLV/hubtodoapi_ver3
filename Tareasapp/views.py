import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from Tareasapp.models import Tareas
from Tareasapp.serializers import TareasSerializer
# Create your views here.



@csrf_exempt
def tareas_api(request,id=0):
    if request.method == 'GET':
        tarea = Tareas.objects.all()
        tarea_serializer = TareasSerializer(tarea,many=True)
        return JsonResponse(tarea_serializer.data,safe=False)
    elif request.method == 'POST':
        tarea_data = JSONParser().parse(request)
        tarea_serializer = TareasSerializer(data=tarea_data)
        if tarea_serializer.is_valid():
            tarea_serializer.save()
            return JsonResponse({"mensaje":"agregada correctamente"},safe=False)
        return JsonResponse({"mensaje":"fallo al agregar"},safe=False)
    elif request.method == 'PUT':
        tarea_data = JSONParser().parse(request)
        tarea = Tareas.objects.get(id_tarea = tarea_data['id_tarea'])
        tarea_serializer = TareasSerializer(tarea, data=tarea_data)
        if tarea_serializer.is_valid():
            tarea_serializer.save()
            return JsonResponse({"mensaje":"tarea actualizada correctamente"},safe=False)
    elif request.method == 'DELETE':
        tarea = Tareas.objects.get(id_tarea=id)
        tarea.delete()
        return JsonResponse({"mensaje":"tarea eliminada correctamente"},safe=False)

