from rest_framework import  serializers
from authentication.models import Usuarios

    

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True)
   
    
    class Meta:
         model = Usuarios
         fields = ['id', 'first_name', 'last_name', 'username']