from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status


#Hacer las vistas del API_REST de usuarios
class UserViewSets(viewsets.ModelViewSet):
    #variables
    queryset= CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]

    #agregar la seguridad con las siguiente variables
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    #que metodos va a proteger
    def get_permissions(self):
        if self.request.method in ['POST','PUT','DELETE']:
            return[IsAuthenticated()]
        return[]
    
    def destroy(self, request, *args, **kwargs):
        user_to_delete = self.get_object()

        # Si el usuario autenticado es el mismo que el usuario que intenta eliminarse, lo bloqueamos
        if request.user == user_to_delete:
            return Response(
                {"error": "No puedes eliminarte a ti mismo."},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().destroy(request, *args, **kwargs)


#Hacer una vista que devuelva el token
from rest_framework_simplejwt.views import TokenObtainPairView
class CustomTokenObteinPairView(TokenObtainPairView):
    serializer_class= CustomTokenObtainPairSelializer

from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 

class CustomUserFormAPI(APIView):

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        fields = {
            field: {
                'label': form[field].label,
                'input': form[field].field.widget.attrs,
                'type': form[field].field.widget.input_type,
            }
            for field in form.fields 
        }
        return Response(fields)

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.data)
        if form.is_valid():
            user_data = form.cleaned_data
            User = get_user_model()
            user = User.objects.create_user(
                email=user_data['email'],
                password=user_data['password1'],  # Aquí usamos 'password1' en lugar de 'password'
                name=user_data['name'],
                surname=user_data['surname'],
                control_number=user_data['control_number'],
                age=user_data['age'],
                tel=user_data['tel'],
            )
            return Response({'message': 'Usuario creado con éxito'}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)