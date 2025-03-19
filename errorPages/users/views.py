from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.renderers import JSONRenderer

#Hacer las vistas del API_REST de usuarios
class UserViewSets(viewsets.ModelViewSet):
    #se necesitan tres variables para hacer una vista
    #queryset que es para hacer la consulta
    queryset = CustomUser.objects.all()
    #serializer que es para hacer la serializacion
    serializer_class = CustomUserSerializer
    #renderizar respuesta que es para hacer la respuesta
    renderer_classes = [JSONRenderer]
    
    #si quieres agregar la parte de seguridad
    #pon estas 2 variables
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    #que metodos va a proteger
    #GET,POST,PUT,DELETE
    def get_permissions(self):
        if self.request.method in ['POST,PUT,DELETE']:
            return [IsAuthenticated()]
        return []
        
#Hacer una vista que me devueva mi Token
from rest_framework_simplejwt.views import TokenObtainPairView
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer