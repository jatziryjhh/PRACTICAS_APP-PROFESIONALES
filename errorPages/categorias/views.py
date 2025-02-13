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