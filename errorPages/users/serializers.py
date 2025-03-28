from .models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.renderers import JSONRenderer

#Serializador para el API_REST
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields='__all__'
        
#Serializador para los tokens
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        #cosas que el token va a  regresa      
        token['email'] = user.email
        #se pueden agregar mas campos
        return token