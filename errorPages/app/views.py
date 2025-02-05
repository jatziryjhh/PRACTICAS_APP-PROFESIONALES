from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import ErrorLog, Usuarios
from .utils import google_search

""" def index(request):
    return HttpResponse("<h1>Hola Mundo !</h1>") """

def index(request):
    return render(request,'index.html', status=200)

def error_404_view(request,exception):
    return render(request,'404.html', status=404)

def error_500_view(request,exception):
    return render(request,'404.html', status=500)

def generar_error(request,exception):
    return 0/7

def onepage(request):
    return render(request,'onepage.html', status=200)

def prueba_front (request):
    
    # del front al back
    texto = request.GET.get('texto','')
    #el primer GET es el metodo y el segundo get es el metodo de la clase request
    
    #vamos a generar informacion en python para enviarla al template
    objeto1={
        'id':'001',
        'titulo':'primer titulo1',
        'descripcion':'texto generico 1'
    }
    objeto2={
        'id':'002',
        'titulo':texto,
        'descripcion':'texto generico 2'
    }
    objeto3={
        'id':'003',
        'titulo':'primer titulo3',
        'descripcion':'texto generico 3'
    }
    
    conjunto = [objeto1,objeto2,objeto3]
    
    #esto es despues de hacer lo de la base,vamos a obtener los datos de la base, haciendo la importacion de Usuarios o bueno tu base
    personas=Usuarios.objects.values('id','nombres','apellidos','edad') #esto es para obtener los datos de la base de datos
    listaPersonas=list(personas)
    
    #como mandar un objeto (variable) de python a la vista
    return render(
        request,
        'prueba.html',
        { 'objeto1':objeto1,'arreglo':conjunto,'lista':listaPersonas }
    )
    
def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})

#esto es para la practica
def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})