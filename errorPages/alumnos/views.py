from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Alumnos
from .serializers import AlumnosSerializer

#clase que serializa los alumnos
class AlumnosViewset(viewsets.ModelViewSet):
    #me dice de donde saco el mmodelo y la informacion de bd
    queryset = Alumnos.objects.all()
    #como serializar la informacion
    serializer_class = AlumnosSerializer
    #como se va a renderizar la informacion
    renderer_classes = [JSONRenderer]
    
    #permite filtrar que metodos HTTP se puede usar
    #GET, POST, PUT, DELETE
    #por defecto si no lo declaro, se usan todos
    #http_method_names = ['GET', 'POST', 'PUT', 'DELETE']