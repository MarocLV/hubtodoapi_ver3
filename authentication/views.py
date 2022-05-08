import email
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator

from .serializers import UserSerializer
from .models import Usuarios
from Tareasapp.serializers import TareasSerializer
from rest_framework.views import APIView


from rest_framework import status
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate, login

from .authTokentodoapp import CsrfExemptSessionAuthentication, BasicAuthentication

# Create your views here.

class UsuarioView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    #Esta función corrige el error por csrf, se puede omitir cuando en el formulario se agrega csrf token
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        """Con esta función se pueden registrar usuarios en la base de datos, recibe un JSON con los
        atributos: 'name','last_name','email','password'
        La contraseña se encripta con la función make_password()
        Al ser usada con el método POST y con los datos del JSON correctos,
        Retorna un estado 200 y el mensaje "Exito"
        La ruta utilizada es '/api/auth/register'"""
        
        if request.method == 'POST':
            jd = json.loads(request.body)
            Usuarios.objects.create(username=jd['username'], first_name=jd['first_name'],last_name=jd['last_name'],email=jd['email'],
            password=make_password(jd['password']))
            datos={'mensaje':'Exito'}
            return JsonResponse(datos) 
        else:
            datos={'mensaje':'Aquí se registran usuarios'}
            return JsonResponse(datos)  
        

class Login(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        email = request.data.get('email', None)            
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        return Response({'error': 'contraseña o usuario incorrecto'},status=status.HTTP_400_BAD_REQUEST)

class CustomUserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuarios.objects.all()