from django.db import models
from categorias.models import Categoria

class DetallesProducto(models.Model):
    #atributos de la clase
    descripcion = models.CharField(max_length=300)
    fecha_caducidad = models.DateField()
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)    
    
#clase de productos
class Producto(models.Model):
    #atributos de la clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    Imagen = models.URLField()
    
    #primer parametro es el modelo a relacionar,y despues la estrategia de borrado
    detalles_producto = models.OneToOneField(DetallesProducto,null=True,blank=True, on_delete=models.CASCADE)
    #cuando se requiera hacer una relación se usa un campo:
    #OneToOneField (1:1)
    #ForeignKey (1:M)
    categoria = models.ForeignKey(Categoria,null=True,blank=True, on_delete=models.SET_NULL)
    #ManyToManyField (M:M)
    proveedor=models.ManyToManyField(Proveedor)
    def __str__(self):
        return self.nombre
    
    #Necesito una funcion que devuelva el objeto en forma de Dict
    def to_dict(self):
        return {
            #claveValor:"valor"
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.Imagen
        }
