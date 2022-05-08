from django.contrib.auth.models import AbstractUser
from django.db import models
#from Tareasapp.serializers import TareasSerializer


# Create your views here.
class Usuarios(AbstractUser):
    """
        Profile user model
    """
    email = models.EmailField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    def get_full_name_user(self):
        return {'full_name': f"{self.first_name} {self.last_name}"}
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

"""class Login(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        username = request.data.get('username', None)            
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        return Respo
        """
