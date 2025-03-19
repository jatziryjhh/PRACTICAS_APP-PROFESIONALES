from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from .forms import ProductoForm
from django.shortcuts import render, redirect

#clase que serializa los productos
class ProductoViewset(viewsets.ModelViewSet):
    #me dice de donde saco el mmodelo y la informacion de bd
    queryset = Producto.objects.all()
    #como serializar la informacion
    serializer_class = ProductoSerializer
    #como se va a renderizar la informacion
    renderer_classes = [JSONRenderer]
    
    #permite filtrar que metodos HTTP se puede usar
    #GET, POST, PUT, DELETE
    #por defecto si no lo declaro, se usan todos
    #http_method_names = ['GET', 'POST']
    
def agregar_view(request):
   form = ProductoForm()
   return render(request, 'agregar.html', {'form': form})
