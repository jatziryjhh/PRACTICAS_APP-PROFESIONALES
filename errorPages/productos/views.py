from django.shortcuts import render,redirect
from .models import Producto
from .forms import ProductoForm

#este objeto me permite devolver un objeto en forma de JSON
from django.http import JsonResponse


#Vista que devuleve los Productos en forma de JSON
#este diccionario fue creado al aire y no es seguro
def lista_productos(request):
    #obtengo todos los productos
    productos = Producto.objects.all()
    #guaradar los datos en un dict
    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.Imagen
        }
        
        for p in productos
    ]
    return JsonResponse(data, safe=False)
    
def ver_productos(request):
    return render(request, 'ver.html')

def agregar_producto(request):
    #checar si vengo del formulario
    if request.method == 'POST':
        #quiere decir que se envio el formulario
        form = ProductoForm(request.POST)
        #checcar que sus datos sean validos
        if form.is_valid():
            #lo guardo en la base de datos
            form.save()
            return redirect('ver')
        
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})

import json
#funcione que agrega un producto con un objeto JSON
def registrar_producto(request):
    #checar si nuestra request es de tipo POST
    if request.method == 'POST':
        #quiere decir que si estoy manejando el request
        try:
            data=json.loads(request.body) #parametro es un texto que deberia ser un JSON
            #creo un nuevo producto
            producto=Producto.objects.create(
                nombre=data['nombre'],
                precio=data['precio'],
                Imagen=data['Imagen']
            ) #create directamente mete el objeto en la BD
            #devolver un mensaje de exito
            return JsonResponse(
                {
                'mensaje':'Registro exitoso',
                'id':producto.id,
                },status=201)
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {
                'error':str(e),
                },status=400
            )
    #si no es post el request
    return JsonResponse(
        {
        'error':'El metodo no esta soportado',
        },status=405
    )        
       