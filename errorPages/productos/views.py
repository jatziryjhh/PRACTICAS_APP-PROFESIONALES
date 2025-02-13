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