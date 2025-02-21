from django.shortcuts import render,redirect
from .models import Categoria
from django.http import JsonResponse
from .forms import CategoriaForm


def lista_categorias(request):
    categorias = Categoria.objects.all()
    data=[
        {'nombre':c.nombre,'imagen':c.imagen}
        for c in categorias
    ]
    return JsonResponse(data, safe=False)

def ver_categorias(request):
    return render(request, 'ver_categorias.html') 

def crear_categoria(request):
    #checar si vengo del formulario
    if request.method == 'POST':
        #quiere decir que se envio el formulario
        form = CategoriaForm(request.POST)
        #checcar que sus datos sean validos
        if form.is_valid():
            #lo guardo en la base de datos
            form.save()
            return redirect('ver')
        
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

import json
#funcione que agrega un categoria con un objeto JSON
def registrar_categorias(request):
    #checar si nuestra request es de tipo POST
    if request.method == 'POST':
        #quiere decir que si estoy manejando el request
        try:
            data=json.loads(request.body) #parametro es un texto que deberia ser un JSON
            #creo un nuevo categoria
            categoria=Categoria.objects.create(
                nombre=data['nombre'],
                imagen=data['imagen']
            ) #create directamente mete el objeto en la BD
            #devolver un mensaje de exito
            return JsonResponse(
                {
                'mensaje':'Registro exitoso',
                'id':categoria.id,
                },status=201)
        except Exception as e:
            return JsonResponse({'error':str(e),},status=400)
    #si no es post el request
    return JsonResponse({'error':'El metodo no esta soportado',},status=405) 