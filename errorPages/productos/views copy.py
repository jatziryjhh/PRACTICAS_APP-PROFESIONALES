from django.shortcuts import render,redirect
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import get_object_or_404


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

#funciones para el método PUT
def actualizar_producto(request,id_producto):
    #checar si nuestra request es de tipo PUT
    if request.method == 'PUT':
        producto=get_object_or_404(Producto,id=id_producto)
        try:
            #la informacion de la modificacion del producto viene del body del request
            data=json.loads(request.body)
            #actualizo el producto
            producto.nombre=data.get('nombre',producto.nombre)
            producto.precio=data.get('precio',producto.precio)
            producto.Imagen=data.get('Imagen',producto.Imagen)
            producto.save()
            return JsonResponse(
                {
                'mensaje':'Actualizacion exitosa'
                },status=200)
        except Exception as e:
            return JsonResponse(
                {
                'error':str(e),
                },status=400
            )
    #si no es put el request
    return JsonResponse({'error':'El metodo no es PUT'},status=405)
            
#funciones para delete
def borrar_producto(request,id_producto):
    if request.method == 'DELETE':
        producto=get_object_or_404(Producto,id=id_producto)
        producto.delete() #<!-- borra fisicamente el registro de la BD
        return JsonResponse({'mensaje':'Producto eliminado'},status=200)
    return JsonResponse({'error':'El metodo no es DELETE',},status=405)
        
#funcion adicional para get
#de retornar un producto en especifico
def obtener_producto(request,id_producto):
    if request.method == 'GET':
        producto=get_object_or_404(Producto,id=id_producto)
        data={
            'nombre':producto.nombre,
            'precio':producto.precio,
            'Imagen':producto.Imagen
        }
        return JsonResponse(data,status=200)
    return JsonResponse({'error':'El metodo no es GET'},status=405)

